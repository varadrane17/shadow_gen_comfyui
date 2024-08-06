import cv2
import numpy as np
from .utils import to_torch_array
from torchvision.transforms import functional as F
import torch
from PIL import Image

class FGOverlay:

    RETURN_TYPES = ("IMAGE",)


    FUNCTION = 'run'
    
    CATEEGORY = "FGOverlay"

    @classmethod
    def INPUT_TYPES(cls):
        return{
            "required" :{
                "image":("IMAGE",),
                "mask" : ("MASK",)
            },
        }
    
    def run(self, image, mask):
        image = F.to_pil_image(image[0].permute(2, 0, 1))
        mask = F.to_pil_image(mask[0])
        background = Image.new("RGB", image.size, color=(255, 255, 255))
        composite_image = Image.composite(image, background, mask)
        composite_image_arr = (
            torch.from_numpy(np.array(composite_image)).unsqueeze(0) / 255.0
        )
        return (composite_image_arr,)

