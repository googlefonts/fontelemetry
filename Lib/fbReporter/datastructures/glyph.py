# -------------------------------
# Base classes
# -------------------------------
class GlyphBase(object):
    def __init__(self, name, glyphunicode):
        self.name = name
        self.unicode = glyphunicode

    def get_name(self):
        return self.name

    def get_unicode(self):
        return self.unicode

    def get_color_value(self):
        raise NotImplementedError


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
