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

import argparse
import os
import runpy
import sys

from fontelemetry import __version__

import fontTools
import glyphsLib


def main():
    argv = sys.argv
    if len(argv) == 1:
        sys.stderr.write(
            "[ERROR] Missing arguments to fontelemetry!{}".format(os.linesep)
        )
        sys.exit(1)
    # argparse parser
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-v", "--version", help="display version number", action="store_true"
    )

    args = parser.parse_args()

    # command line logic implementation
    if args.version:
        print("fontelemetry v{}".format(__version__))
        sys.exit(0)

    # TODO: implement execution of module-specific code as command suite
    module = "fontelemetry." + argv[0]

    runpy.run_module(module, run_name="__main__")


if __name__ == "__main__":
    sys.exit(main())
