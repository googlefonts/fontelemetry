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

from glyphsLib import GSFont
from fontTools.ufoLib import UFOReader

from fontelemetry.datastructures.source import GlyphsSource, UFOSource


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
