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

from fontelemetry.datastructures.glyph import GlyphDummyObj


# -----------------------
# Base classes
# -----------------------
class Source(object):
    """A source specification specific object that holds source data.

    The Source object is instantiated with an external library object that
    is instantiated on source read and used to manipulate source file data
    along with object attributes that maintain the original source file path
    and define a retrievable calling code defined unique ID field.

    Attributes:
        obj: (instance-specific) A source file object that is instantiated with an external library
        path: (string) source file or directory path
        id: (string) unique ID for an instantiated Source object

    For glyphs source, the object is a glyphsLib.GSFont object.
    For UFO source, the object is a fontTools.ufoLib.glifLib.GlyphSet object
    """

    def __init__(self, source_object, path=None, source_id=None):
        """Inits Source object with source file read data from external libraries.

        Args:
            source_object: (instance-specific) A source file object that is instantiated with an external library
            path: (string) path to file or directory used to instantiate source_object
            source_id: (string) unique ID value for this object
        """
        self.obj = source_object
        self.path = path
        self.id = source_id

    def __repr__(self):
        return "({} v{} is defined as: {})".format(
            self.__class__, __version__, self.__dict__
        )

    def __str__(self):
        return "{}".format(self.__dict__)

    def get_source_path(self):
        """Returns source path attribute string."""
        return self.path


# ------------------------------------
# Inherited classes
# ------------------------------------
class GlyphsSource(Source):
    """See base class."""

    def __init__(self, source_object, path=None, source_id=None):
        Source.__init__(self, source_object, path=path, source_id=source_id)

    def yield_ordered_glyphobj(self):
        for glyph in self.obj.glyphs:
            yield glyph


class UFOSource(Source):
    """See base class."""

    def __init__(self, source_object, path=None, source_id=None):
        Source.__init__(self, source_object, path=path, source_id=source_id)


class UFOGlyphSetSource(Source):
    """See base class."""

    def __init__(self, source_object, path=None, source_id=None):
        Source.__init__(self, source_object, path=path, source_id=source_id)

    def yield_ordered_glyphobj(self):
        for glif in self.obj.contents:
            gobj = GlyphDummyObj()
            self.obj.readGlyph(glif, glyphObject=gobj)
            yield gobj


