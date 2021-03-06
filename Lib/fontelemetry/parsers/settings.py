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

import io

from fontelemetry.parsers.toml import parse_toml_file, parse_toml_string


def parse_settings(filepath=None, toml_string=None):
    """Parses a toml formatted settings file to a Python dictionary.

    Args:
        filepath: (string, default) path to settings file
        toml_string: (string, optional) toml formatted string

    Returns:
        Dictionary with parsed toml data.
    """
    if filepath is not None:
        with io.open(filepath, "r") as f:
            return parse_toml_file(f)
    elif toml_string is not None:
        return parse_toml_string(toml_string)
    else:
        return None
