#!/usr/bin/env python3
# coding=utf-8

# Wypisać w pętli liczby od 0 do 30 z wyjątkiem liczb podzielnych przez 3. Użyć pętli for lub while.

for num in range(0, 31):
    if not ((num % 3) == 0):
        print(num)