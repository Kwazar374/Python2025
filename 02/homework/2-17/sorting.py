#!/usr/bin/env python3
# coding=utf-8

# Posortować wyrazy ze stringu line raz alfabetycznie, a raz pod względem długości. Wskazówka: funkcja wbudowana sorted().

line = "A FFFFFF CCC DDDD AAAAAAAA BBBB EEEEE BB"
words = line.split()
sorted_alphabetically = sorted(words)
sorted_by_length = sorted(words, key=len)

print(f"Wyrazy posortowane alfabetycznie: {sorted_alphabetically}")
print(f"Wyrazy posortowane według długości: {sorted_by_length}")

assert sorted_alphabetically == ['A', 'AAAAAAAA', 'BB', 'BBBB', 'CCC', 'DDDD', 'EEEEE', 'FFFFFF']
assert sorted_by_length == ['A', 'BB', 'CCC', 'DDDD', 'BBBB', 'EEEEE', 'FFFFFF', 'AAAAAAAA']

