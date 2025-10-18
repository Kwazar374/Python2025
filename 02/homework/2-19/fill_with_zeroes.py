#!/usr/bin/env python3
# coding=utf-8

# Na liście L mamy liczby jedno-, dwu- i trzycyfrowe dodatnie. Chcemy zbudować string z trzycyfrowych bloków, gdzie liczby jedno- i dwucyfrowe będą miały blok dopełniony zerami, np. 007, 024. Wskazówka: str.zfill().

integers = [1, 23, 456, 78, 9, 10, 111, 213, 3, 45]
filled_strings = [str(integer).zfill(3) for integer in integers]
result = "".join(filled_strings)

print(f"String z liczb dopełnionych zerami: {result}")
assert result == "001023456078009010111213003045"