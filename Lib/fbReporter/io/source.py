# Library version
from fbReporter import __version__

import io

from glyphsLib import GSFont
from fontTools.ufoLib import UFOReader

from fbReporter.datastructures.source import GlyphsSource, UFOSource


# -----------------------
# Base classes
# -----------------------
class SourceReader(object):
    def __init__(self, path, source_id):
        self.path = path
        self.source_id = source_id

    def __repr__(self):
        return "({} v{} is defined as: {})".format(self.__class__, __version__, self.__dict__)

    def __str__(self):
        return "{}".format(self.__dict__)

    def read(self):
        raise NotImplementedError


# ------------------------------------
# Inherited classes
# ------------------------------------
class GlyphsSourceReader(SourceReader):
    def __init__(self, path, source_id=None):
        SourceReader.__init__(self, path, source_id)

    def read(self):
        return GlyphsSource(GSFont(self.path), path=self.path, source_id=self.source_id)


class UFOSourceReader(SourceReader):
    def __init__(self, filepath, source_id=None):
        SourceReader.__init__(self, filepath, source_id)

    def read(self):
        return UFOSource(UFOReader(self.path), path=self.path, source_id=self.source_id)
