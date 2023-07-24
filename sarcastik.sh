#!/usr/bin/env bash
#
# Copyright (c) 2023 Sven Varkel.
#
CURDIR=$(dirname "$0")
pbpaste|python3 random_case/random_case.py|pbcopy
