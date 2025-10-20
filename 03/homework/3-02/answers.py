#!/usr/bin/env python3
# coding=utf-8
# Co jest złego w kodzie:

# 1)
L = [3, 5, 4] ; L = L.sort()

# odp: Metoda sort() sortuje listę in-place i zwraca None. Przypisanie wyniku do L powoduje, że L staje się None.

# 2)
x, y = 1, 2, 3

# odp: po lewej stronie są dwie zmienne, a po prawej trzy wartości. Przy przypisaniu wystąpi błąd.

# 3)
X = 1, 2, 3 ; X[1] = 4

# odp: Krotki są niemodyfikowalne, więc próba przypisania wartości do elementu krotki spowoduje błąd.

# 4)
X = [1, 2, 3] ; X[3] = 4

# odp: Indeks 3 jest poza zakresem listy, która ma indeksy 0, 1, 2. Próba przypisania do tego indeksu spowoduje błąd.

# 5)
X = "abc" ; X.append("d")

# odp: stringi nie mają metody append(). Próba wywołania tej metody spowoduje błąd.

# 6)
L = list(map(pow, range(8)))

# odp: funkcja pow wymaga dwóch argumentów, a map przekazuje tylko jeden (element z range(8)). Pojawi się błąd.