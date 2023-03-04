#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import platform

# current version of pyambi
__version__ = "0.5.0"

# current os platform (Linux, Darwin or Windows)
OS = platform.uname()[0]

# Go version required for schemer2
GO_VERSION_REQUIRED = "go1.15.8"

# Go download url for each platform
GO_LINUX_DOWNLOAD_URL = "https://golang.org/dl/" + GO_VERSION_REQUIRED + ".linux-amd64.tar.gz"
GO_DARWIN_DOWNLOAD_URL = "https://golang.org/dl/" + GO_VERSION_REQUIRED + ".darwin-amd64.pkg"
GO_WINDOWS_DOWNLOAD_URL = "https://golang.org/dl/" + GO_VERSION_REQUIRED + ".windows-amd64.msi"

# Schemer2 repository information
SCHEMER2_REPOSITORY = "github.com/0xARK/schemer2"

# basic command for run pyambi project
RUN_PYAMBI = "python3 pyambi.py"

# pip required dependencies
PIP_DEPENDENCIES = ["opencv-python", "argparse", "urllib3", "numpy", "mss", "Pillow"]
