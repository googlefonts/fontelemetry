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

import os
import sys
from fontelemetry.datastructures.color import GlyphsAppColor, GlyphsAppColorDefMap


# Base classes
class ColorDefParser(object):
    """Base class for glyph mark color definition parsers.

    Attributes:
        settings: settings dictionary that follows fontelemetry settings specification
        colordef_map: fontelemetry.datastructures.color.GlyphsAppColorDefMap
        colordef_settings: settings["colordefinitions"][SOURCE FORMAT] field of settings
    """

    def __init__(self, settings):
        """Inits ColorDefParser."""
        self.settings = settings
        self.colordef_map = None
        self.colordef_settings = None

    def __repr__(self):
        return "({} v{} is defined as: {})".format(
            self.__class__, __version__, self.__dict__
        )

    def __str__(self):
        return "{}".format(self.__dict__)

    def _define_parser_colordef_attr(self):
        raise NotImplementedError

    def parse(self):
        """Parses data for glyph mark color definitions and returns a
        fontelemetry.datastructures.color.GlyphsAppColorDefMap."""
        raise NotImplementedError


# Inherited classes
class ColorDefParserGlyphs(ColorDefParser):
    """Parses glyph mark color definitions from glyphs source files.

    Attributes:
        settings: settings dictionary that follows fontelemetry settings specification
        colordef_map: fontelemetry.datastructures.color.GlyphsAppColorDefMap
        colordef_settings: settings["colordefinitions"][SOURCE FORMAT] field of settings
    """

    def __init__(self, settings):
        """Inits ColorDefParserGlyphs."""
        ColorDefParser.__init__(self, settings)
        self.valid_colors = [
            member.name for name, member in GlyphsAppColor.__members__.items()
        ]
        self._define_parser_colordef_attr()

    def _define_parser_colordef_attr(self):
        self.colordef_map = GlyphsAppColorDefMap()
        self.colordef_settings = self.settings["colordefinitions"]["glyphs"]

    def parse(self):
        """Parses data for glyph mark color definitions in glyphs source files
        and returns a fontelemetry.datastructures.color.GlyphsAppColorDefMap."""
        for color in self.colordef_settings:
            if color in self.valid_colors:
                # retrieve the color definition from the settings data
                definition_value = self.colordef_settings[color]
                # define the GlyphsAppColorDefMap with the updated color definition
                self.colordef_map.set_color_value(color, definition_value)
            else:
                sys.stderr.write(
                    "Settings contain the color '{}' which is not a valid color!  Ignored...{}".format(
                        color, os.linesep
                    )
                )

        return self.colordef_map
