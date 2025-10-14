#!/usr/bin/env python3
# coding=utf-8

text = "Python Yeti Tiger Hippo Orangutan Narwhal"
words = text.split()
longest_word = max(words, key=len)
print(f"Najdłuższe słowo to {longest_word}. Jego długość to {len(longest_word)}.")
assert longest_word == "Orangutan"