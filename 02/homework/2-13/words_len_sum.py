#!/usr/bin/env python3
# coding=utf-8

text = "Python Yeti Tiger Hippo Orangutan Narwhal"

words = text.split()
lengths = [len(word) for word in words]
total_length = sum(lengths)

print(f"Suma długości słów to {total_length}.")
assert total_length == 36