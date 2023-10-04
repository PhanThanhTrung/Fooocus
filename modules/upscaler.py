import os
from collections import OrderedDict
from typing import Tuple

import torch
from torch.cuda import OutOfMemoryError as OOM_EXCEPTION

import comfy.utils as comfyutils
from comfy_extras.chainner_models.architecture.RRDB import RRDBNet


class UpScaler():
    def __init__(self, model_path: str, device: str = "cpu") -> None:
        self.model = self._load_model(model_path=model_path, device=device)
        self.device = device

    def _load_model(self, model_path: str, device: str) -> RRDBNet:
        assert os.path.exists(model_path), "Model doesn't exist!"
        sd = torch.load(model_path)
        sdo = OrderedDict()
        for k, v in sd.items():
            sdo[k.replace('residual_block_', 'RDB')] = v
        model = RRDBNet(sdo)
        model.to(device)
        model.eval()
        return model

    def perform_upscale(self, image: torch.Tensor) -> Tuple:
        in_img = image.movedim(-1, -3).to(self.device)

        tile = 512
        overlap = 32

        oom = True
        s = None
        while oom:
            try:
                steps = in_img.shape[0] * comfyutils.get_tiled_scale_steps(
                    in_img.shape[3], in_img.shape[2], tile_x=tile, tile_y=tile, overlap=overlap)
                pbar = comfyutils.ProgressBar(steps)
                s = comfyutils.tiled_scale(in_img, lambda a: self.model(
                    a), tile_x=tile, tile_y=tile, overlap=overlap, upscale_amount=self.model.scale, pbar=pbar)
                oom = False
            except OOM_EXCEPTION as e:
                tile //= 2
                if tile < 128:
                    raise e
        if s is not None:
            s = torch.clamp(s.movedim(-3, -1), min=0, max=1.0)
            return (s,)
        else:
            return (None,)
