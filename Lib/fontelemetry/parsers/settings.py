# Library version
from fontelemetry import __version__

import io

from fontelemetry.parsers.toml import parse_toml_file, parse_toml_string


def parse_settings(filepath=None, toml_string=None):
    if filepath is not None:
        with io.open(filepath, "r") as f:
            return parse_toml_file(f)
    elif toml_string is not None:
        return parse_toml_string(toml_string)
    else:
        return None

