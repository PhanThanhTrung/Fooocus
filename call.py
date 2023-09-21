from gradio_client import Client

client = Client("http://127.0.0.1:7861/", serialize=False)
result = client.predict(
				"Stalin russia!",	# str in 'parameter_8' Textbox component
				"Howdy!",	# str in 'Negative Prompt' Textbox component
				["Fooocus V2", "Surrealism"],	# List[str] in 'Image Style' Checkboxgroup component
				"Speed",	# str in 'Performance' Radio component
				"704×1408",	# str in 'Aspect Ratios' Radio component
				1,	# int | float (numeric value between 1 and 32) in 'Image Number' Slider component
				5,	# int | float in 'Seed' Number component
				0,	# int | float (numeric value between 0.0 and 30.0) in 'Sampling Sharpness' Slider component
				"sd_xl_base_1.0_0.9vae.safetensors",	# str (Option from: []) in 'SDXL Base Model' Dropdown component
				"sd_xl_refiner_1.0_0.9vae.safetensors",	# str (Option from: ['None']) in 'SDXL Refiner' Dropdown component
				"sd_xl_offset_example-lora_1.0.safetensors",	# str (Option from: ['None']) in 'SDXL LoRA 1' Dropdown component
				0.5,	# int | float (numeric value between -2 and 2) in 'Weight' Slider component
				"None",	# str (Option from: ['None']) in 'SDXL LoRA 2' Dropdown component
				0.5,	# int | float (numeric value between -2 and 2) in 'Weight' Slider component
				"None",	# str (Option from: ['None']) in 'SDXL LoRA 3' Dropdown component
				0.5,	# int | float (numeric value between -2 and 2) in 'Weight' Slider component
				"None",	# str (Option from: ['None']) in 'SDXL LoRA 4' Dropdown component
				0.5,	# int | float (numeric value between -2 and 2) in 'Weight' Slider component
				"None",	# str (Option from: ['None']) in 'SDXL LoRA 5' Dropdown component
				0.5,	# int | float (numeric value between -2 and 2) in 'Weight' Slider component
				False,	# bool in 'Input Image' Checkbox component
				"Howdy!",	# str in 'parameter_30' Textbox component
				"Disabled",	# str in 'Upscale or Variation:' Radio component
				None,	# str (filepath or URL to image) in 'Drag above image to here' Image component
				[],	# List[str] in 'Outpaint' Checkboxgroup component
				None,	# str (filepath or URL to image) in 'Drag above image to here' Image component
				fn_index=13
)
