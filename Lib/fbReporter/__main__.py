import argparse
import os
import runpy
import sys

from fbReporter import __version__

import fontTools
import glyphsLib


def main():
    argv = sys.argv
    if len(argv) == 1:
        sys.stderr.write(
            "[ERROR] Missing arguments to fb-reporter!{}".format(os.linesep)
        )
        sys.exit(1)
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-v", "--version", help="display version number", action="store_true"
    )

    args = parser.parse_args()

    # VERSION
    if args.version:
        print("fb-reporter v{}".format(__version__))
        sys.exit(0)

    # TODO: implement execution of module-specific code as command suite
    module = "fbReporter." + argv[0]

    runpy.run_module(module, run_name="__main__")


if __name__ == "__main__":
    sys.exit(main())
