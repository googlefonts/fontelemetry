# Library version
from fontelemetry import __version__

import os
import sys
from fontelemetry.datastructures.color import GlyphsAppColor, GlyphsAppColorDefMap


# Base classes
class ColorDefParser(object):
    def __init__(self, settings):
        self.settings = settings
        self.colordef = None

    def __repr__(self):
        return "({} v{} is defined as: {})".format(self.__class__, __version__, self.__dict__)

    def __str__(self):
        return "{}".format(self.__dict__)

    def _define_parser_attr(self):
        raise NotImplementedError

    def parse(self):
        raise NotImplementedError


# Inherited classes
class ColorDefParserGlyphs(ColorDefParser):
    def __init__(self, settings):
        ColorDefParser.__init__(self, settings)
        self.valid_colors = [
            member.name for name, member in GlyphsAppColor.__members__.items()
        ]
        self._define_parser_attr()

    def _define_parser_attr(self):
        self.colordef_map = GlyphsAppColorDefMap()
        self.colordef_settings = self.settings["colordefinitions"]["glyphs"]

    def parse(self):
        for color in self.colordef_settings:
            if color in self.valid_colors:
                # retrieve the color definition from the settings data
                definition_value = self.colordef_settings[color]
                # define the GlyphsAppColorDefMap with the updated color definition
                self.colordef_map.set_color_value(color, definition_value)
            else:
                sys.stderr.write(
                    "[Font Bakery Reporter] Settings contain the color '{}' which is not a valid color!  Ignored...{}".format(
                        color, os.linesep
                    )
                )

        return self.colordef_map
