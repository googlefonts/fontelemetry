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

from enum import Enum

# Library version
from fontelemetry import __version__


# -------------------------------
# Base classes
# -------------------------------
class ColorDefMapBase(object):
    """Base class for glyph mark color definition mapped objects.

    These objects are containers for key:value mapping of
    color name : user-specified definition for the color name.
    """

    def __init__(self):
        pass

    def __repr__(self):
        return "({} v{} is defined as: {})".format(
            self.__class__, __version__, self.__dict__
        )

    def __str__(self):
        return "{}".format(self.__dict__)

    def get_color_hex(self, color_name):
        """Returns the hexadecimal formatted color encoding for a color value.

        Args:
            color_name: (string) a color name that should match the self.[color_name] class attribute

        Returns:
            A hexadecimal formatted color value formatted as a string
        """
        raise NotImplementedError

    def get_color_rgba(self, color_name):
        """Returns the RGBA formatted color encoding for a color value.

        Args:
            color_name: (string) a color name that should match the self.[color_name] class attribute

        Returns:
            A RBGA formatted color value formatted as a string
        """
        raise NotImplementedError

    def get_color_value(self, color_name):
        """Returns the user-specified definition value for a color name.

        Args:
            color_name: (string) A color name that should match the self.[color_name] class attribute

        Returns:
            A definition value for the color name formatted as a string
        """
        raise NotImplementedError

    def set_color_value(self, color_name, value):
        """Sets the user-specified definition value for a color name.

        Args:
            color_name: (string) A color name that should match the self.[color_name] class attribute
            value: (string) A definition value for the color_name
        """
        raise NotImplementedError


class GlyphsAppColorDefMap(ColorDefMapBase):
    """See base class."""

    def __init__(self):
        ColorDefMapBase.__init__(self)
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


class UFOColorDefMap(ColorDefMapBase):
    """See base class."""
    def __init__(self):
        pass



# -----------------------------------
# Glyphs App specific color object
# -----------------------------------
class GlyphsAppColor(Enum):
    """Contains Glyphs application specific glyph mark color data definitions.

    The color name is mapped to the GlyphsApp integer index value for the
    `color` fields in the *.glyphs source file specification
    """

    red = 0
    orange = 1
    brown = 2
    yellow = 3
    ltgreen = 4
    dkgreen = 5
    ltblue = 6
    dkblue = 7
    purple = 8
    pink = 9
    ltgrey = 10
    dkgrey = 11
    white = 12  # this is an uncolored glyph
