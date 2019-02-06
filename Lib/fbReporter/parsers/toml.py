# Library version
from fbReporter import __version__

import toml


def parse_toml(file_object):
    return toml.load(file_object)

