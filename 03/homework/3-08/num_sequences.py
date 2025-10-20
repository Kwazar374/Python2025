#!/usr/bin/env python3
# coding=utf-8

# Dla dwóch sekwencji liczb lub znaków znaleźć:
# (a) listę elementów występujących jednocześnie w obu sekwencjach (bez powtórzeń),
# (b) listę wszystkich elementów z obu sekwencji (bez powtórzeń).

seq1 = [1, 2, 3, 4, 5, 2, 8, 8]
seq2 = [4, 5, 6, 7, 4, 8, 8, 9]

# a) elementy wspólne obu sekwencji (bez powtórzeń)
wspolne = list(set(seq1) & set(seq2))

# b) wszystkie elementy z obu sekwencji (bez powtórzeń)
wszystkie = list(set(seq1) | set(seq2))

print("Elementy wspólne obu sekwencji (bez powtórzeń):", wspolne)
print("Wszystkie elementy (bez powtórzeń):", wszystkie)

assert sorted(wspolne) == [4, 5, 8]
assert sorted(wszystkie) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
