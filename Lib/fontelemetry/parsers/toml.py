# Library version
from fontelemetry import __version__

import toml


def parse_toml_file(file_object):
    return toml.load(file_object)


def parse_toml_string(toml_string):
    return toml.loads(toml_string)
