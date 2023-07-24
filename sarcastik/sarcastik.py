#  Copyright (c) 2023 Sven Varkel.
#
# This simple script takes string from stdin and randomizes it's case.
# It can be used with command line tools to paste from clipboard and return converted string to clipboard.
#
#
import re
import sys
import random


def randomize_case(s):
    a = re.split(r"(\w)", s.strip())
    rnd = random.randint(1, 666666)
    b = map(lambda x: x.upper() if x and (ord(x) + rnd) % 2 == 0 else x.lower(), a)
    out = "".join(b)
    return out


for line in sys.stdin:
    s = line.strip()
    out = randomize_case(s)
    sys.stdout.write(out + "\n")
    sys.exit(0)
