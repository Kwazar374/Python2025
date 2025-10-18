#!/usr/bin/env python3
# coding=utf-8

# Na liście L znajdują się liczby całkowite dodatnie. Stworzyć string będący ciągiem cyfr kolejnych liczb z listy L.

integers = [1, 2, 3, 46, 5]
string_representation = "".join(str(i) for i in integers)

print(f"Lista liczb jako string: {string_representation}")
assert string_representation == "123465"