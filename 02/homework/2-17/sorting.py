#!/usr/bin/env python3
# coding=utf-8

line = "A FFFFFF CCC DDDD AAAAAAAA BBBB EEEEE BB"
words = line.split()
sorted_alphabetically = sorted(words)
sorted_by_length = sorted(words, key=len)

print(f"Wyrazy posortowane alfabetycznie: {sorted_alphabetically}")
print(f"Wyrazy posortowane według długości: {sorted_by_length}")
