import nodes

"""


    Simple utility custom nodes for ComfyUI regarding experimentation with SDXL
    
    By Jens Jakob Kramhøft

    Copyright (c) 2023  

"""

MANIFEST = {
    "name": "JJKUtil",
    "version": (0,1,1),
    "author": "Jens Jakob Kramhøft",
    "project": "https://github.com/jjkramhoeft/util-nodes-for-comfyui",
    "description": "A small node suite for ComfyUI",
}

#---------------------------------------------------------------------------------------------------------------------------------------------------#

class SDXLRecommendedImageSize:
    RESOLUTIONS = ["Cinema (1536x640)", "Widescreen (1344x768)", "Photo (1216x832)", "TV (1152x896)", "Square (1024x1024)"]
    ASPECT = ["Landscape", "Portrait"]

    @classmethod
    def INPUT_TYPES(s):
        return {"required": {
                    "resolution": (SDXLRecommendedImageSize.RESOLUTIONS, {"default": "Square (1024x1024)"}),
                    "aspect": (SDXLRecommendedImageSize.ASPECT, {"default": "Portrait"})
                    },
                }

    RETURN_TYPES = ("INT", "INT", )
    RETURN_NAMES = ("width", "height", )
    FUNCTION = "get_value"

    CATEGORY = "jjk"

    def get_value(self, resolution, aspect, ):
        if resolution == "Cinema (1536x640)":
            if aspect == "Landscape":
                return (1536, 640)
            else:
                return (640, 1536)
        if resolution == "Widescreen (1344x768)":
            if aspect == "Landscape":
                return (1344, 768)
            else:
                return (768, 1344)
        if resolution == "Photo (1216x832)":
            if aspect == "Landscape":
                return (1216, 832)
            else:
                return (832, 1216)
        if resolution == "TV (1152x896)":
            if aspect == "Landscape":
                return (1152, 896)
            else:
                return (896, 1152)
        if resolution == "Square (1024x1024)":
            return (1024, 1024)

#---------------------------------------------------------------------------------------------------------------------------------------------------#

class JjkText:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"text": ("STRING", {"multiline": True})}}
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text",)
    FUNCTION = "get_value"
    CATEGORY = "jjk"

    def get_value(self, text):
        return (text,)

#---------------------------------------------------------------------------------------------------------------------------------------------------#

class JjkShowText:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text": ("STRING", {"forceInput": True}),
            }
        }
    
    INPUT_IS_LIST = True
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text",)
    FUNCTION = "show_value"
    CATEGORY = "jjk"
    OUTPUT_NODE = True
    OUTPUT_IS_LIST = (True,)

    def show_value(self, text):
        print(f"show text: {text}")
        return {"ui": {"text": text}, "result": (text,)}


#---------------------------------------------------------------------------------------------------------------------------------------------------#

class JjkConcat:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "delimmitor": (["none", "space", "comma"],),
            },
            "optional": {
                "text1": ("STRING", {"forceInput": True}),
                "text2": ("STRING", {"forceInput": True}),      
                "text3": ("STRING", {"forceInput": True}),      
                "text4": ("STRING", {"forceInput": True}),      
                "text5": ("STRING", {"forceInput": True}),       
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text",)
    FUNCTION = "get_value"
    CATEGORY = "jjk"

    def get_value(self, delimmitor, text1=None, text2=None, text3=None, text4=None, text5=None):
        needdelim = False
        delim = ""
        if delimmitor == "space":
            delim = " "
        if delimmitor == "comma":
            delim = ", "

        concatenated = ""

        if text1:
            concatenated = text1
            needdelim = True
        
        if text2:
            if needdelim:
                concatenated += delim
            concatenated += text2
            needdelim = True
        
        if text3:
            if needdelim:
                concatenated += delim
            concatenated += text3
            needdelim = True

        if text4:
            if needdelim:
                concatenated += delim
            concatenated += text4
            needdelim = True

        if text5:
            if needdelim:
                concatenated += delim
            concatenated += text5
            needdelim = True

        return (concatenated,)

#---------------------------------------------------------------------------------------------------------------------------------------------------#




# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "SDXLRecommendedImageSize": "SDXL Recommended image sizes",
    "JjkText": "Text",
    "JjkShowText": "ShowText",
    "JjkConcat": "Concatenate",
}
