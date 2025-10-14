#!/usr/bin/env python3
# coding=utf-8

text = "GvR GVR GvR gvr"
text = text.replace("GvR", "Guido van Rossum")

print(text)
assert text == "Guido van Rossum GVR Guido van Rossum gvr"