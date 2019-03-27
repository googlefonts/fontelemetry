# Copyright 2019 Fontelemetry Authors and Contributors

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Library version
from fontelemetry import __version__


# --------------------------------
# Dummy class for fontTools writes
# --------------------------------
class GlyphDummyObj(object):
    def __init__(self):
        pass


# -------------------------------
# Base classes
# -------------------------------
class GlyphBase(object):
    """Base class for Glyph objects.

    Attributes:
        name: glyph name as a string
        unicode: glyph Unicode hexademical code point as a string or None if non-encoded glyph
    """

    def __init__(self, name, glyphunicode):
        """Inits GlyphBase with name and unicode attributes."""
        self.name = name
        self.unicode = glyphunicode

    def __repr__(self):
        return "({} v{} is defined as: {})".format(
            self.__class__, __version__, self.__dict__
        )

    def __str__(self):
        return "{}".format(self.__dict__)

    def get_name(self):
        """Returns GlyphBase object name attribute.

        Returns:
            glyph name attribute value as a string
        """
        return self.name

    def get_unicode(self):
        """Returns GlyphBase object unicode attribute.

        Returns:
            glyph unicode attribute value as a string or None if the glyph is not Unicode encoded
        """
        return self.unicode


# ------------------------------
# Inherited Classes
# ------------------------------

# -------------------
# mark color objects
# -------------------
class GlyphColorHex(GlyphBase):
    """GlyphBase object that contains hexademical mark color data and associated mark color definition value for a glyph.

    Attributes:
        hexcolor: (string) hexadecimal formatted color value
        value: (string) user-defined definition for the color
        """

    def __init__(self, glyphname=None, glyphunicode=None, hexcolor=None, value=None):
        """Inits GlyphColorHex object with hexadecimal color and color definition values.

        Args:
            glyphname: (string) glyph name
            glyphunicode: (string) glyph Unicode code point hexadecimal string or None if not Unicode-encoded
            hexcolor: (string) hexadecimal formatted color value
            value: (string) user-defined definition of the color value used for the instantaiated GlyphBase object
        """
        GlyphBase.__init__(self, glyphname, glyphunicode)
        self.hexcolor = hexcolor
        self.value = value

    def get_color(self):
        """Returns hexademical formatted color value for GlyphColorHex object."""
        return self.hexcolor

    def get_color_definition(self):
        """Returns the definition that is mapped to the glyph mark color value."""
        return self.value


class GlyphColorRGB(GlyphBase):
    """GlyphBase object that contains RGB mark color data and associated mark color definition value for a glyph.

    Attributes:
        rgbcolor: (string) RGB formatted color value
        value: (string) user-defined definition for the color
    """

    def __init__(self, glyphname=None, glyphunicode=None, rgbcolor=None, value=None):
        """Inits GlyphColorRGB object with RGB color and color definition values.

        Args:
            glyphname: (string) glyph name
            glyphunicode: (string) glyph Unicode code point hexadecimal string or None if not Unicode-encoded
            rgbcolor: (string) RGB formatted color value as
            value: (string) user-defined definition of the color value used for the instantaiated GlyphBase object
        """
        GlyphBase.__init__(self, glyphname, glyphunicode)
        self.rgb = rgbcolor
        self.value = value

    def get_color(self):
        """Returns RGB formatted color value for GlyphColorHex object."""
        return self.rgb

    def get_color_definition(self):
        """Returns the definition that is mapped to the glyph mark color value."""
        return self.value


class GlyphColorRGBA(GlyphBase):
    """GlyphBase object that contains RGBA mark color data and associated mark color definition value for a glyph.

    Attributes:
        rgbacolor: (string) hexadecimal formatted color value
        value: (string) user-defined definition for the color
    """

    def __init__(self, glyphname=None, glyphunicode=None, rgbacolor=None, value=None):
        """Inits GlyphColorRGBA object with RGBA color and color definition values.

        Args:
            glyphname: (string) glyph name
            glyphunicode: (string) glyph Unicode code point hexadecimal string or None if not Unicode-encoded
            rgbacolor: (string) RGBA formatted color value as
            value: (string) user-defined definition of the color value used for the instantaiated GlyphBase object
        """
        GlyphBase.__init__(self, glyphname, glyphunicode)
        self.rgba = rgbacolor
        self.value = value

    def get_color(self):
        """Returns RGBA formatted color value for GlyphColorHex object."""
        return self.rgba

    def get_color_definition(self):
        """Returns the definition that is mapped to the glyph mark color value."""
        return self.value
