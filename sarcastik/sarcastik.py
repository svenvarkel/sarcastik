#  Copyright (c) 2023 Sven Varkel.
#
# This simple script takes string from stdin and randomizes it's case.
# It can be used with command line tools to paste from clipboard and return converted string to clipboard.
#
#
import re
import sys
import random
import argparse


def randomize_case(s):
    # a = re.split(r"(\w)", s.strip().lower())
    a = list(s.strip())
    rnd = random.randint(1, 666)
    b = map(
        lambda x: x[1].lower()
        if x[1] and (ord(x[1]) + rnd + x[0]) % 5 == 0
        else x[1].upper(),
        enumerate(a),
    )
    out = "".join(b)
    return out


parser = argparse.ArgumentParser(description="Sarcastik")
parser.add_argument("str", type=str, nargs="?", help="String to be converted")
args = parser.parse_args()
out = None
if args.str:
    out = randomize_case(args.str)
else:
    for line in sys.stdin:
        out = randomize_case(line)
        break

sys.stdout.write(out + "\n")
sys.exit(0)
