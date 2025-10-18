#!/usr/bin/env python3
# coding=utf-8

# W tekście znajdującym się w stringu line zamienić ciąg znaków "GvR" na "Guido van Rossum".

text = "GvR GVR GvR gvr"
text = text.replace("GvR", "Guido van Rossum")

print(text)
assert text == "Guido van Rossum GVR Guido van Rossum gvr"