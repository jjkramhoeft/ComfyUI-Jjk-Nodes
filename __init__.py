import os
import shutil

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

THIS_DIR=os.path.dirname(os.path.abspath(__file__))
DIR_DEV_JS=os.path.abspath(f'{THIS_DIR}/js')
DIR_PY=os.path.abspath(f'{THIS_DIR}/py')
DIR_WEB_JS=os.path.abspath(f'{THIS_DIR}/../../web/extensions/jjk_util')

if not os.path.exists(DIR_WEB_JS):
    os.makedirs(DIR_WEB_JS)

shutil.copytree(DIR_DEV_JS, DIR_WEB_JS, dirs_exist_ok=True)

print("jjk_util loding")
