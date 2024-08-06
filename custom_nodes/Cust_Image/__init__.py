from .fg_over_bg import FGBGOverlay
from .fg_over_white import FGOverlay

NODE_CLASS_MAPPINGS = {
    "FGBGOverlay": FGBGOverlay,
    "FGOverlay": FGOverlay
}

NODE_DISPLAY_NAME_MAPPINGS ={
    "FGOverlay": "FGOverlay",
    "FGBGOverlay" : "FGBGOverlay"
}