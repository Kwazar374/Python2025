#!/usr/bin/env python3
# coding=utf-8

integers = [1, 2, 3, 46, 5]
string_representation = "".join(str(i) for i in integers)

print(f"Lista liczb jako string: {string_representation}")
assert string_representation == "123465"