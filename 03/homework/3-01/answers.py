#!/usr/bin/env python3
# coding=utf-8
# Czy podany kod jest poprawny składniowo w Pythonie? Jeśli nie, to dlaczego?

# 1)

x = 2; y = 3;
if (x > y):
    result = x;
else:
    result = y;

# odp: Tak, powyższy kod jest poprawny składniowo, chociaż użycie średników jest zbędne w Pythonie.

# 2)

# for i in "axby": if ord(i) < 100: print (i) # Zakomentowano, żeby uniknąć warningów VSC

# odp: Nie, powyższy kod nie jest poprawny składniowo.
# Bezpośrednie umieszczenie instrukcji 'if' po dwukropku nie jest dozwolone w powyższym przypadku.
# Jednak są przypadki gdzie jest to dozwolone, np. w list comprehension.

# 3)

for i in "axby": print (ord(i) if ord(i) < 100 else i)

# Tak, powyższy kod jest poprawny składniowo.