"""
Generate header file with macros defining MicroPython version info.

# CIRCUITPY-CHANGE: This script is thoroughly reworked for use with CircuitPython.
This script works with Python 3.7 and newer
"""

from __future__ import print_function

import argparse
import sys
import os
import pathlib
import datetime
import subprocess

# CIRCUITPY-CHANGE: Factor out version computation to py/version.py
import version


# CIRCUITPY-CHANGE
def cannot_determine_version():
    raise SystemExit(
        """Cannot determine version.

CircuitPython must be built from a git clone with tags.
If you cloned from a fork, fetch the tags from adafruit/circuitpython as follows:

    make fetch-tags"""
    )


def make_version_header(repo_path, filename):
    # Get version info using git (required)
    info = version.get_version_info_from_git(repo_path)
    if info is None:
        cannot_determine_version()
    git_tag, git_hash, ver = info
    if len(ver) < 3:
        cannot_determine_version()
    else:
        version_string = ".".join(ver)

    build_date = datetime.date.today()
    if "SOURCE_DATE_EPOCH" in os.environ:
        build_date = datetime.datetime.utcfromtimestamp(
            int(os.environ["SOURCE_DATE_EPOCH"])
        ).date()

    # Generate the file with the git and version info
    # CIRCUITPY-CHANGE: different contents
    file_data = """\
// This file was generated by py/makeversionhdr.py
#define MICROPY_GIT_TAG "%s"
#define MICROPY_GIT_HASH "%s"
#define MICROPY_BUILD_DATE "%s"
#define MICROPY_VERSION_MAJOR (%s)
#define MICROPY_VERSION_MINOR (%s)
#define MICROPY_VERSION_MICRO (%s)
#define MICROPY_VERSION_PRERELEASE 0
#define MICROPY_VERSION_STRING "%s"
// Combined version as a 32-bit number for convenience
#define MICROPY_VERSION (MICROPY_VERSION_MAJOR << 16 | MICROPY_VERSION_MINOR << 8 | MICROPY_VERSION_MICRO)
#define MICROPY_FULL_VERSION_INFO "Adafruit CircuitPython " MICROPY_GIT_TAG " on " MICROPY_BUILD_DATE "; " MICROPY_BANNER_MACHINE
""" % (
        git_tag,
        git_hash,
        build_date.strftime("%Y-%m-%d"),
        ver[0].replace("v", ""),
        ver[1],
        ver[2],
        version_string,
    )

    # Check if the file contents changed from last time
    write_file = True
    if os.path.isfile(filename):
        with open(filename, "r") as f:
            existing_data = f.read()
        if existing_data == file_data:
            write_file = False

    # Only write the file if we need to
    if write_file:
        print("GEN %s" % filename)
        with open(filename, "w") as f:
            f.write(file_data)


def main():
    parser = argparse.ArgumentParser()
    # makeversionheader.py lives in repo/py, so default repo_path to the
    # parent of sys.argv[0]'s directory.
    parser.add_argument(
        "-r",
        "--repo-path",
        default=os.path.join(os.path.dirname(sys.argv[0]), ".."),
        help="path to MicroPython Git repo to query for version",
    )
    parser.add_argument("dest", nargs=1, help="output file path")
    args = parser.parse_args()

    make_version_header(args.repo_path, args.dest[0])


if __name__ == "__main__":
    main()
