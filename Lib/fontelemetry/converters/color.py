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

import math


def get_upscaled_rgb_tuple(downscaled_rgb_tuple):
    """Scales an RGB color object from decimal 0.0-1.0 to int 0-255.

    Based on source by Greg Taylor in the python-colormath library
    https://github.com/gtaylor/python-colormath/blob/1d168613718d2d7d31ec4230524e987ef66823c7/colormath/color_objects.py#L565
    and used under the BSD license."""
    rgb_r_down, rgb_g_down, rgb_b_down = downscaled_rgb_tuple
    rgb_r = int(math.floor(0.5 + rgb_r_down * 255))
    rgb_g = int(math.floor(0.5 + rgb_g_down * 255))
    rgb_b = int(math.floor(0.5 + rgb_b_down * 255))
    return rgb_r, rgb_g, rgb_b

