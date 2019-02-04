import os
import runpy
import sys

import fontTools
import glyphsLib


def main():
    argv = sys.argv
    if len(argv) == 1:
        sys.stderr.write("[ERROR] Missing arguments to fb-reporter!{}".format(os.linesep))
        sys.exit(1)
    # TODO : add support for --help, --usage, --version options
    module = "fbReporter." + argv[0]

    runpy.run_module(module, run_name="__main__")


if __name__ == "__main__":
    sys.exit(main())
