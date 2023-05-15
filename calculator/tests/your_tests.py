#!/usr/bin/env python3
from calculator_adapter import run


### ADD AT LEAST TWO TESTS HERE!

assert run("90 + 13").output == "103"

assert run("50 - 69").output == "-19"

assert run("7 * 16").output == "112"

assert run("200 / 40").output == "5"

###

print("All tests passed!")
