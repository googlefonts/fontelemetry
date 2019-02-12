# Library version
from fontelemetry import __version__


# -----------------------
# Base classes
# -----------------------
class Source(object):
    def __init__(self, source_object, path=None, source_id=None):
        self.obj = source_object
        self.path = path
        self.id = source_id

    def __repr__(self):
        return "({} v{} is defined as: {})".format(self.__class__, __version__, self.__dict__)

    def __str__(self):
        return "{}".format(self.__dict__)

    def get_source_path(self):
        return self.path

    def yield_ordered_glyphobj(self):
        raise NotImplementedError


# ------------------------------------
# Inherited classes
# ------------------------------------
class GlyphsSource(Source):
    def __init__(self, source_object, path=None, source_id=None):
        Source.__init__(self, source_object, path=path, source_id=source_id)

    def yield_ordered_glyphobj(self):
        for glyph in self.obj.glyphs:
            yield glyph


class UFOSource(Source):
    def __init__(self, source_object, path=None, source_id=None):
        Source.__init__(self, source_object, path=path, source_id=source_id)

    def yield_ordered_glyphobj(self):
        # TODO
        pass




