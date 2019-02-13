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
    def __init__(self, glyphname=None, glyphunicode=None, hexcolor=None, value=None):
        GlyphBase.__init__(self, glyphname, glyphunicode)
        self.hexcolor = hexcolor
        self.value = value

    def get_color(self):
        return self.hexcolor

    def get_color_definition(self):
        return self.value


class GlyphColorRGB(GlyphBase):
    def __init__(self, glyphname=None, glyphunicode=None, rgbcolor=None, value=None):
        GlyphBase.__init__(self, glyphname, glyphunicode)
        self.rgb = rgbcolor
        self.value = value

    def get_color(self):
        return self.rgb

    def get_color_definition(self):
        return self.value


class GlyphColorRGBA(GlyphBase):
    def __init__(self, glyphname=None, glyphunicode=None, rgbacolor=None, value=None):
        GlyphBase.__init__(self, glyphname, glyphunicode)
        self.rgba = rgbacolor
        self.value = value

    def get_color(self):
        return self.rgba

    def get_color_definition(self):
        return self.value
