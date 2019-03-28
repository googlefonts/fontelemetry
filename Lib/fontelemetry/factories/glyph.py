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

from fontelemetry.datastructures.color import GlyphsAppColor
from fontelemetry.datastructures.glyph import GlyphColorHex, GlyphColorRGBA
from fontelemetry.datastructures.source import (
    GlyphsSource,
    UFOSource,
    UFOGlyphSetSource,
)
from fontelemetry.factories.base import FactoryBase
from fontelemetry.parsers.colordef import ColorDefParserGlyphs, ColorDefParserUFO


# --------------------------------
# Inherited classes
# --------------------------------
class OrderedGlyphColorListFactory(FactoryBase):
    """Returns an Python list containing instantiated
    fontelemetry.datastructures.glyph.GlyphColor[Format] objects.

    Attributes:
        glyphssource_valid_color_specs: valid color format specs in glyphs source
        ufosource_valid_color_specs: valid color format specs in UFO source
        source_obj: A fontelemetry.datastructures.source.Source derived object
        source_type: source type label string (either "glyphs" or "ufo")
        settings: settings dictionary that follows fontelemetry settings specification
        color_spec: color format specification used to define the GlyphColor[Format] objects ("hex" or "rgba")

    """

    def __init__(self, source_obj, settings=None, color_spec=None):
        FactoryBase.__init__(self)
        self.glyphssource_valid_color_specs = ["hex", "rgba"]
        self.ufosource_valid_color_specs = ["rgba"]
        self.source_obj = source_obj
        if type(self.source_obj) is GlyphsSource:
            self.source_type = "glyphs"
        elif type(self.source_obj) is UFOSource:
            self.source_type = "ufo"
        elif type(self.source_obj) is UFOGlyphSetSource:
            self.source_type = "ufogs"
        else:
            self.source_type = None
        self.settings = settings
        self.color_spec = color_spec
        self._msg_fail_instantiation = (
            "Failed instantiation of OrderedGlyphColorListFactory"
        )

        # instantiation validations
        # -- did not define source object
        if self.source_type is None:
            raise TypeError(
                "{}.  Invalid source object!".format(self._msg_fail_instantiation)
            )
        # -- did not define valid glyphs source color specification
        if (
            self.source_type == "glyphs"
            and self.color_spec not in self.glyphssource_valid_color_specs
        ):
            raise TypeError(
                "{}.  Invalid color specification for glyphs source. Did not include a value in {}!".format(
                    self._msg_fail_instantiation, self.glyphssource_valid_color_specs
                )
            )
        # -- did not define valid UFO source color specification
        if (
            self.source_type == "ufogs"
            and self.color_spec not in self.ufosource_valid_color_specs
        ):
            raise TypeError(
                "{}.  Invalid color specification for UFO source. Did not include a value in {}!".format(
                    self._msg_fail_instantiation, self.ufosource_valid_color_specs
                )
            )
        # -- did not define colordef settings
        if self.settings is None:
            raise TypeError(
                "{}.  Did not receive color definition settings on instantiation!".format(
                    self._msg_fail_instantiation
                )
            )

    def _get_glyphcolor_obj(self, glyphname, glyphunicode, glyphcolor, colorvalue):
        if self.color_spec == "hex":
            return GlyphColorHex(glyphname, glyphunicode, glyphcolor, colorvalue)
        elif self.color_spec == "rgba":
            return GlyphColorRGBA(glyphname, glyphunicode, glyphcolor, colorvalue)
        else:
            return None

    def _get_glyphs_mapped_colordef_settings(self):
        cpd = ColorDefParserGlyphs(self.settings)
        return cpd.parse()

    def _get_ufo_mapped_colordef_settings(self):
        cpd = ColorDefParserUFO(self.settings)
        return cpd.parse()

    def get(self):
        """Returns an ordered list of instantiated fontelemetry.datastructures.GlyphColor[Format] objects
        based upon glyph order in source file(s), glyph mark color in source file(s), and color definitions
        indicated at OrderedGlyphColorListFactory instantiation time."""
        glyphcolorobj_list = []

        if self.source_type == "glyphs":
            colordef_settings = self._get_glyphs_mapped_colordef_settings()
            for source_glyph in self.source_obj.yield_ordered_glyphobj():
                # define glyph attributes from:
                #  - glyphs source file read (in self.source_obj)
                #  - color : value settings mapping (in colordef_settings)
                glyphname = source_glyph.name
                glyphunicode = source_glyph.unicode
                glyph_color_index = source_glyph.color
                # define as "white" if source_glyph.color object is None
                # or outside bounds.  GlyphsApp default source write approach
                # is to exclude color value in the source when glyph is uncolored=white
                # so the source_glyph.color value is defined as None
                if glyph_color_index is None or glyph_color_index > 12:
                    glyph_color_index = 12
                glyph_color_name = GlyphsAppColor(glyph_color_index).name
                if self.color_spec == "hex":
                    glyphcolor = colordef_settings.get_color_hex(glyph_color_name)
                elif self.color_spec == "rgba":
                    glyphcolor = colordef_settings.get_color_rgba(glyph_color_name)
                else:
                    glyphcolor = None
                glyph_color_value = colordef_settings.get_color_value(glyph_color_name)
                glyphcolorobj_list.append(
                    self._get_glyphcolor_obj(
                        glyphname, glyphunicode, glyphcolor, glyph_color_value
                    )
                )
            return glyphcolorobj_list
        elif self.source_type == "ufogs":
            colordef_settings = self._get_ufo_mapped_colordef_settings()
            for glyph in self.source_obj.yield_ordered_glyphobj():
                glyph_name = glyph.name

                if hasattr(glyph, "lib"):
                    glyph_lib = glyph.lib

                    if "public.markColor" in glyph_lib:
                        glyph_rgba = glyph_lib["public.markColor"]
                    else:
                        glyph_rgba = None
                else:
                    glyph_rgba = None

                if hasattr(glyph, "unicodes"):
                    glyph_unicode = hex(glyph.unicodes[0])
                else:
                    glyph_unicode = None

                # define the glyph-specific color indicator value from the
                # settings file
                glyph_color_value = ""
                # if there is no RGBA value defined, it is a "white" uncolored
                # glyph in the editor, so we define with the white definition
                if glyph_rgba is None:
                    color_def_white = getattr(colordef_settings, "white")
                    glyph_color_value = color_def_white["value"]
                else:
                    # for glyphs with color, pull the color value definition
                    # that was entered in the settings file
                    for color in colordef_settings.__dict__.keys():
                        color_def = getattr(colordef_settings, color)
                        if glyph_rgba == color_def["rgba"]:
                            glyph_color_value = color_def["value"]

                # TODO: include validation for missing color values

                glyphcolorobj_list.append(
                    self._get_glyphcolor_obj(
                        glyph_name, glyph_unicode, glyph_rgba, glyph_color_value
                    )
                )

            return glyphcolorobj_list
