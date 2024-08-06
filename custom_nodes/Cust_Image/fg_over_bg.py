

import cv2
import numpy as np
from .utils import to_torch_array
from torchvision.transforms import functional as F
import torch
from PIL import Image

class FGBGOverlay:

    RETURN_TYPES = ("IMAGE",)


    FUNCTION = 'run'
    
    CATEEGORY = "FGBGOverlay"

    @classmethod
    def INPUT_TYPES(cls):
        return{
            "required" :{
                "image_fg":("IMAGE",),
                "image_bg" : ("IMAGE",),
            },
        }
    
    def run(self, image_fg, image_bg):
        image_FG = F.to_pil_image(image_fg[0].permute(2, 0, 1)).convert("RGBA")
        image_BG = F.to_pil_image(image_bg[0].permute(2, 0, 1)).convert("RGBA")
        composite_image = Image.alpha_composite(image_BG,image_FG)
        composite_image_arr = (
            torch.from_numpy(np.array(composite_image)).unsqueeze(0) / 255.0
        )
        return (composite_image_arr,)

