from enum import Enum


# -------------------------------
# Base classes
# -------------------------------
class ColorDefBase(object):
    def __init__(self):
        pass

    def get_color_hex(self, color_name):
        raise NotImplementedError

    def get_color_rgba(self, color_name):
        raise NotImplementedError

    def get_color_value(self, color_name):
        raise NotImplementedError

    def set_color_value(self, color_name, value):
        raise NotImplementedError


# -----------------------------------
# Glyphs App specific color objects
# -----------------------------------
class GlyphsAppColor(Enum):
    RED = 0
    ORANGE = 1
    BROWN = 2
    YELLOW = 3
    LTGREEN = 4
    DKGREEN = 5
    LTBLUE = 6
    DKBLUE = 7
    PURPLE = 8
    PINK = 9
    LTGREY = 10
    DKGREY = 11
    WHITE = 12  # this is an uncolored glyph


class GlyphsAppColorDef(ColorDefBase):
    def __init__(self):
        ColorDefBase.__init__(self)
        self.red = {"hex": "E9B8A8", "rgba": (233, 184, 168, 1.00), "value": None}
        self.orange = {"hex": "F9D9B3", "rgba": (249, 217, 178, 1.00), "value": None}
        self.brown = {"hex": "D9CAB3", "rgba": (217, 202, 178, 1.00), "value": None}
        self.yellow = {"hex": "FBF4B7", "rgba": (251, 244, 183, 1.00), "value": None}
        self.ltgreen = {"hex": "E3F8C7", "rgba": (227, 248, 200, 1.00), "value": None}
        self.dkgreen = {"hex": "B3D1AA", "rgba": (179, 209, 170, 1.00), "value": None}
        self.ltblue = {"hex": "B3D6FA", "rgba": (180, 214, 250, 1.00), "value": None}
        self.dkblue = {"hex": "9BB0EF", "rgba": (155, 176, 239, 1.00), "value": None}
        self.purple = {"hex": "C5A8E5", "rgba": (199, 171, 230, 1.00), "value": None}
        self.pink = {"hex": "F5C2DC", "rgba": (246, 195, 220, 1.00), "value": None}
        self.ltgrey = {"hex": "E6E6E5", "rgba": (230, 229, 229, 1.00), "value": None}
        self.dkgrey = {"hex": "B2B3B3", "rgba": (178, 178, 178, 1.00), "value": None}
        self.white = {"hex": "FFFFFF", "rgba": (255, 255, 255, 1.00), "value": None}

    def get_color_hex(self, color_name):
        color_needle = getattr(self, color_name)
        return color_needle["hex"]

    def get_color_rgba(self, color_name):
        color_needle = getattr(self, color_name)
        return color_needle["rgba"]

    def get_color_value(self, color_name):
        color_needle = getattr(self, color_name)
        return color_needle["value"]

    def set_color_value(self, color_name, value):
        color_needle = getattr(self, color_name)
        color_needle["value"] = str(value)
        setattr(self, color_name, color_needle)
