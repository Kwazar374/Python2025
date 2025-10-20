#!/usr/bin/env python3
# coding=utf-8

# Napisać program rysujący prostokąt zbudowany z małych kratek.
# Należy zbudować pełny string, a potem go wypisać.

import sys

def rysuj_prostokat(wysokosc: int, szerokosc: int) -> None:

    kreska_z_plusikow = ""
    kreska_z_separatorow = ""

    kreska_z_plusikow += "+---" * szerokosc
    kreska_z_separatorow += "|   " * szerokosc
    
    kreska_z_plusikow += "+\n"
    kreska_z_separatorow += "|\n"

    prostokat = ""
    prostokat += (kreska_z_plusikow + kreska_z_separatorow) * wysokosc
    prostokat += kreska_z_plusikow

    print(prostokat)

wymiary_od_uzytkownika = input("Podaj wymiary prostokata oddzielone spacją ('wysokosc, szerokosc'): ")
try:
    wymiary_prostokata = [int(wymiar) for wymiar in wymiary_od_uzytkownika.split()]
    if not len(wymiary_prostokata) == 2:
        print("\nNieprawidłowa liczba wymiarów (należy podać dwa wymiary: wysokość i szerokość)!\n")
        sys.exit(1)
    if (not wymiary_prostokata[0] > 0) or (not wymiary_prostokata[1] > 0):
        print("\nWymiary nie są liczbami dodatnimi!")
        sys.exit(1)
except ValueError:
    print("\nPodane wymiary nie są liczbami całkowitymi.\n")
    sys.exit(1)

print(f"\nOto prostokąt o wymiarach {wymiary_prostokata[0]}x{wymiary_prostokata[1]}:\n")
rysuj_prostokat(wymiary_prostokata[0], wymiary_prostokata[1])
