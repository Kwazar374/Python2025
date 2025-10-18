#!/usr/bin/env python3
# coding=utf-8

# Mamy dany string wielowierszowy line. Podać sposób obliczenia liczby wyrazów w stringu. Przez wyraz rozumiemy ciąg "czarnych" znaków, oddzielony od innych wyrazów białymi znakami (spacja, tabulacja, newline).

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