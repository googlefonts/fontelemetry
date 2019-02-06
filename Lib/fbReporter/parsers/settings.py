# Library version
from fbReporter import __version__

import io

from fbReporter.parsers.toml import parse_toml


def parse_settings(filepath):
    with io.open(filepath, "r") as f:
        return parse_toml(f)
