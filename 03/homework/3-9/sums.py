#!/usr/bin/env python3
# coding=utf-8

# Mamy daną listę sekwencji (listy lub krotki) różnej długości zawierających liczby.
# Znaleźć listę zawierającą sumy liczb z tych sekwencji.
# Przykładowa sekwencja [[],[4],(1,2),[3,4],(5,6,7)], spodziewany wynik [0,4,3,7,18].

test_seq = [[],[4],(1,2),[3,4],(5,6,7)]
test_seq2 = [(),(10,2),(1,1,1),[2,2,2,2],(3,3,3,3,3),[2,1,0,-3], (), []]

sums = [sum(seq) for seq in test_seq]
sums2 = [sum(seq) for seq in test_seq2]
print(f"Suma liczb w poszczególnych sekwencjach 1: {sums}")
print(f"Suma liczb w poszczególnych sekwencjach 2: {sums2}")

assert sums == [0, 4, 3, 7, 18]
assert sums2 == [0, 12, 3, 8, 15, 0, 0, 0]