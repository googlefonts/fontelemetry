# Library version
from fbReporter import __version__

from fbReporter.datastructures.color import GlyphsAppColor
from fbReporter.datastructures.glyph import GlyphColorHex, GlyphColorRGBA
from fbReporter.datastructures.source import GlyphsSource, UFOSource
from fbReporter.parsers.colordef import ColorDefParserGlyphs


# -----------------------
# Base classes
# -----------------------
class FactoryBase(object):
    def __init__(self):
        pass

    def __repr__(self):
        return "({} v{} is defined as: {})".format(self.__class__, __version__, self.__dict__)

    def __str__(self):
        return "{}".format(self.__dict__)

    def get(self):
        raise NotImplementedError


# --------------------------------
# Inherited classes
# --------------------------------
class OrderedGlyphColorListFactory(FactoryBase):
    def __init__(self, source_obj,  settings=None, color_spec=None):
        FactoryBase.__init__(self)
        self.glyphssource_valid_color_specs = ["hex", "rgba"]
        self.ufosource_valid_color_specs = ["rgba"]
        self.source_obj = source_obj
        if type(self.source_obj) is GlyphsSource:
            self.source_type = "glyphs"
        elif type(self.source_obj) is UFOSource:
            self.source_type = "ufo"
        else:
            self.source_type = None
        self.settings = settings
        self.color_spec = color_spec
        self.msg_fail_instantiation = "Failed instantiation of OrderedGlyphColorListFactory"

        # instantiation validations
        # -- did not define source object
        if self.source_type is None:
            raise TypeError(
                "[Font Bakery Reporter] {}.  Invalid source object!".format(
                    self.msg_fail_instantiation))
        # -- did not define valid glyphs source color specification
        if self.source_type == "glyphs" and self.color_spec not in self.glyphssource_valid_color_specs:
            raise TypeError("[Font Bakery Reporter] {}.  Invalid color specification for glyphs source. Did not include a value in {}!".format(self.msg_fail_instantiation, self.glyphssource_valid_color_specs))
        # -- did not define valid UFO source color specification
        if self.source_type == "ufo" and self.color_spec not in self.ufosource_valid_color_specs:
            raise TypeError("[Font Bakery Reporter] {}.  Invalid color specification for UFO source. Did not include a value in {}!".format(self.msg_fail_instantiation, self.ufosource_valid_color_specs))
        # -- did not define colordef settings
        if self.settings is None:
            raise TypeError(
                "[Font Bakery Reporter] {}.  Did not receive color definition settings on instantiation!".format(
                    self.msg_fail_instantiation))

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
        pass

    def get(self):
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
                glyphcolorobj_list.append(self._get_glyphcolor_obj(glyphname,
                                                                   glyphunicode,
                                                                   glyphcolor,
                                                                   glyph_color_value))
            return glyphcolorobj_list
        elif self.source_type == "ufo":
            # TODO
            pass
