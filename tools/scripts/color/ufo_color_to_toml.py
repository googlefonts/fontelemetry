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

# ======================================================================
#   ufo_color_to_toml.py
#     - Dumps unique UFO *.glif file public.markColor data in toml format
#       that can be used in the fontelemetry settings definition file
#
#   Dependencies: toml, fontTools
#
#   Usage:
#
#     $ python3 ufo_color_to_toml.py [path to UFO directory]
#
# ======================================================================

import os
import sys
import toml
from fontTools.ufoLib.glifLib import GlyphSet


class GlyphDummyObj(object):
    def __init__(self):
        pass


def main(ufo_path):
    glyph_color_list = []
    path_to_ufo_glyphs_dir = os.path.join(ufo_path, "glyphs")
    gs = GlyphSet(path_to_ufo_glyphs_dir)
    for glif in gs.contents:
        gobj = GlyphDummyObj()
        gs.readGlyph(glif, glyphObject=gobj)
        if hasattr(gobj, "lib"):
            glib = gobj.lib
            if "public.markColor" in glib:
                glyph_color_list.append(glib["public.markColor"])

    glyph_color_set = set(glyph_color_list)
    color_dict = {"color": {"mark": {"ufo": {}}}}
    index = 1
    for color in glyph_color_set:
        color_name = "Color{}".format(index)
        color_dict["color"]["mark"]["ufo"][color_name] = []
        color_dict["color"]["mark"]["ufo"][color_name].append(color)
        color_dict["color"]["mark"]["ufo"][color_name].append("Value{}".format(index))
        index += 1

    color_dict["color"]["mark"]["ufo"]["white"] = []
    color_dict["color"]["mark"]["ufo"]["white"].append("1.0,1.0,1.0,1")
    color_dict["color"]["mark"]["ufo"]["white"].append("ValueWhite")

    print(toml.dumps(color_dict))


if __name__ == '__main__':
    main(sys.argv[1])