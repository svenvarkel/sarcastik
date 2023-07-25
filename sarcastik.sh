#!/usr/bin/env bash
#
# Copyright (c) 2023 Sven Varkel.
#
CURDIR=$(dirname "$0")
pbpaste|python3 sarcastik/sarcastik.py|pbcopy
