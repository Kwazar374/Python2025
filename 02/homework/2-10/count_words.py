#!/usr/bin/env python3
# coding=utf-8

line = """
    To jest pewien string zawierajacy spacje
    oraz
    znaki 
    nowej
    linii oraz  nawet   tabulacje
    slow jest tutaj siedemnascie
"""

words = line.split()
words_count = len(words)

print(f"Słów w zadanym stringu jest: {words_count}")
assert words_count == 17