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

from glyphsLib import GSFont
from fontTools.ufoLib import UFOReader
from fontTools.ufoLib.glifLib import GlyphSet

from fontelemetry.datastructures.source import GlyphsSource, UFOSource


# -----------------------
# Base classes
# -----------------------
class SourceReader(object):
    """Reads typeface source and returns an instantiated fontelemetry.datastructures.source.Source object.

    Classes that inherit this base class support glyphs and UFO specified source files.

    Attributes:
        path: path to source file or directory
        source_id: unique ID string for the Source object
    """

    def __init__(self, path, source_id):
        self.path = path
        self.source_id = source_id

    def __repr__(self):
        return "({} v{} is defined as: {})".format(
            self.__class__, __version__, self.__dict__
        )

    def __str__(self):
        return "{}".format(self.__dict__)

    def read(self):
        raise NotImplementedError


# ------------------------------------
# Inherited classes
# ------------------------------------
class GlyphsSourceReader(SourceReader):
    """Reads glyphs format typeface source.

    Attributes:
        path: path to glyphs source file
        source_id: unique ID string for the Source object
    """

    def __init__(self, path, source_id=None):
        SourceReader.__init__(self, path, source_id)

    def read(self):
        """Reads glyphs specified source file from source file path and returns a
        fontelemetry.datastructures.source.GlyphsSource object"""
        return GlyphsSource(GSFont(self.path), path=self.path, source_id=self.source_id)


class UFOSourceReader(SourceReader):
    """Reads UFO format typeface source.

    Attributes:
        path: path to UFO source directory
        source_id: unique ID string for the Source object
    """

    def __init__(self, path, source_id=None):
        SourceReader.__init__(self, path, source_id)

    def read(self):
        """Reads UFO format source file from source file path and returns a
        fontelemetry.datastructures.source.UFOSource object"""
        return UFOSource(UFOReader(self.path), path=self.path, source_id=self.source_id)


class UFOGlyphSetReader(SourceReader):
    """Reads UFO format glif design files.

    Attributes:
        path: path to UFO source directory
        source_id: unique ID string for the Source object
    """

    def __init__(self, path, source_id=None):
        SourceReader.__init__(self, path, source_id)

    def read(self):
        ufo_glyphs_dir_path = os.path.join(self.path, "glyphs")
        return GlyphSet(ufo_glyphs_dir_path)

