# Library version
from fbReporter import __version__

import io

import toml


def parse_settings(filepath):
    with io.open(filepath) as f:
        return toml.load(f)
