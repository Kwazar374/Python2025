#!/usr/bin/env python3
# coding=utf-8

# Znaleźć liczbę cyfr zero w dużej liczbie całkowitej. Wskazówka: zamienić liczbę na string.

number = 1020304050607080900000
number_str = str(number)
zero_count = number_str.count("0")

print(f"Cyfr zero w zadanej liczbie jest {zero_count}.")
assert zero_count == 13