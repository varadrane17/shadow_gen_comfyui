import base64
from io import BytesIO

import numpy as np
import torch
from PIL import Image


def base64_to_img(img_str: str) -> Image.Image:
    return Image.open(BytesIO(base64.b64decode(img_str)))


def img_to_base64(img: Image.Image) -> str:
    buffered = BytesIO()
    img.save(buffered, quality=100, subsampling=0, format="JPEG")
    return base64.b64encode(buffered.getvalue()).decode()


def to_torch_array(image):
    return torch.from_numpy(np.array(image)).unsqueeze(0) / 255.0