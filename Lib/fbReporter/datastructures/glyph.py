# Library version
from fbReporter import __version__


# -------------------------------
# Base classes
# -------------------------------
class GlyphBase(object):
    def __init__(self, name, glyphunicode):
        self.name = name
        self.unicode = glyphunicode

    def __repr__(self):
        return "({} v{} is defined as: {})".format(self.__class__, __version__, self.__dict__)

    def __str__(self):
        return "{}".format(self.__dict__)

    def get_name(self):
        return self.name

    def get_unicode(self):
        return self.unicode


# ------------------------------
# Inherited Classes
# ------------------------------
class GlyphColorHex(GlyphBase):
    def __init__(self, glyphname, glyphunicode, hexcolor, value):
        GlyphBase.__init__(self, glyphname, glyphunicode)
        self.hexcolor = hexcolor
        self.value = value

    def get_color_value(self):
        return self.hexcolor


class GlyphColorRGB(GlyphBase):
    def __init__(self, glyphname, glyphunicode, rgbcolor, value):
        GlyphBase.__init__(self, glyphname, glyphunicode)
        self.rgb = rgbcolor
        self.value = value

    def get_color_value(self):
        return self.rgb


class GlyphColorRGBA(GlyphBase):
    def __init__(self, glyphname, glyphunicode, rgbacolor, value):
        GlyphBase.__init__(self, glyphname, glyphunicode)
        self.rgba = rgbacolor
        self.value = value

    def get_color_value(self):
        return self.rgba
