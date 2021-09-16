#!/usr/bin/env python3

"""Pytekukko setup."""

from setuptools import setup  # type: ignore[import]


def get_version() -> str:
    """Extract version number."""
    fname = "pytekukko/version.py"
    with open(fname, encoding="utf-8") as file_:
        for line in file_:
            if line.startswith("__version__"):
                return line.split("=")[-1].strip("\"'\r\n ")
    raise Exception(f"No __version__ in {fname}!")


if __name__ == "__main__":
    setup(version=get_version())
