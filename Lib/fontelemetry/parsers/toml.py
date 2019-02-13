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

import toml


def parse_toml_file(file_object):
    """Parses toml data using a file-like object to a dictionary.

    Args:
        file_object: (file-like object) file like object instantiated from a toml formatted file

    Returns:
        A dictionary with parsed toml data fields.
    """
    return toml.load(file_object)


def parse_toml_string(toml_string):
    """Parses a toml formatted string to a dictionary.

    Args:
        toml_string: (string) a toml formatted string

    Returns:
        A dictionary with parsed toml data fields.
    """
    return toml.loads(toml_string)
