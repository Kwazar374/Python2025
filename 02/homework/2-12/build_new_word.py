#!/usr/bin/env python3
# coding=utf-8

text = "Python Yeti Tiger Hippo Orangutan Narwhal"

words = text.split()
result = "".join(word[0] for word in words)

print(f"Powstałe słowo to {result}!")
assert result == "PYTHON"