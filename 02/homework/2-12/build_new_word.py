#!/usr/bin/env python3
# coding=utf-8

# Zbudować string stworzony z pierwszych znaków wyrazów ze stringu line. Zbudować napis stworzony z ostatnich znaków wyrazów ze stringu line.

text = "PythonA YetiB TigerC HippoD OrangutanE NarwhalF"

words = text.split()
result1 = "".join(word[0] for word in words)
result2 = "".join(word[-1] for word in words)

print(f"Powstałe słowa to {result1} i {result2}.")
assert result1 == "PYTHON"
assert result2 == "ABCDEF"