#!/usr/bin/env python3
# coding=utf-8

# Napisać program rysujący "miarkę" o zadanej długości. Należy prawidłowo obsłużyć liczby składające się z kilku cyfr (ostatnia cyfra liczby ma znajdować się pod znakiem kreski pionowej). 
# Należy zbudować pełny string, a potem go wypisać.

import sys

def rysuj_miarke(dlugosc: int) -> None:
    # kreski i kropki (pierwszy wiersz)
    podzialka = ""
    for i in range(dlugosc):
        podzialka += "|...."
    podzialka += "|\n"

    # liczby (drugi wiersz)
    numeracja = ""
    for i in range(dlugosc + 1):
        numeracja += str(i)
        spaces = 5 - len(str(i + 1))
        numeracja += " " * spaces

    miarka = podzialka + numeracja
    return miarka

try:
    n = int(input("Podaj długość miarki: "))
    if n <= 0:
        print("Długość miarki musi być liczbą dodatnią.")
        sys.exit(1)
except ValueError:
    print("Podana wartość nie jest liczbą całkowitą.")
    sys.exit(1)

print(rysuj_miarke(n))
