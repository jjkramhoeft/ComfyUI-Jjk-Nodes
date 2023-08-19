from .jjk_util import *

# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "SDXLRecommendedImageSize": SDXLRecommendedImageSize,
    "JjkText": JjkText,
    "JjkShowText": JjkShowText,
    "JjkConcat": JjkConcat,
}


__all__ = ['NODE_CLASS_MAPPINGS']

print("jjk_util loding")
