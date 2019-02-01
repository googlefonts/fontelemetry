import os
import runpy
import sys


def main():
    argv = sys.argv
    if len(argv) == 1:
        sys.stderr.write("[ERROR] Missing arguments!{}".format(os.linesep))
        sys.exit(1)
    # TODO : add support for --help, --usage, --version options
    module = "fbReporter." + argv[0]

    runpy.run_module(module, run_name="__main__")


if __name__ == "__main__":
    sys.exit(main())
