#!/usr/bin/env python3

import sys
import calc

input = " ".join(sys.argv[1:])

print(calc.to_hex(calc.evaluate(input)), end="")
