#!/usr/bin/env python3
# coding=utf-8

# Stworzyć słownik tłumaczący liczby zapisane w systemie rzymskim (z literami I, V, X, L, C, D, M) na liczby arabskie 
# (podać kilka sposobów tworzenia takiego słownika).
# Mile widziany kod tłumaczący całą liczbę [funkcja roman2int()].

print("Tworzenie słownika tłumaczącego liczby rzymskie na arabskie na trzy sposoby:")

# sposob 1: tworzenie słownika "ręcznie"
roman_dict = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}
print(f"Słownik rzymski (sposób 1): {roman_dict}")

# sposób 2: tworzenie słownika za pomocą zip()
letters = "IVXLCDM"
values  = [1, 5, 10, 50, 100, 500, 1000]

roman_dict = dict(zip(letters, values))
print(f"Słownik rzymski (sposób 2): {roman_dict}")

# sposob 3: tworzenie słownika za pomocą dict comprehension
letters = "IVXLCDM"
values  = [1, 5, 10, 50, 100, 500, 1000]

roman_dict = {letter: value for letter, value in zip(letters, values)}
print(f"Słownik rzymski (sposób 3): {roman_dict}\n\n")

# funkcja tłumacząca liczbę rzymską na arabską
import re # import znalazł się tutaj, ponieważ zawartość modułu jest używana w funkcji roman2int i jego obecność w tym miejscu poprawia czytelność kodu

# poniższy wzorzec regex pozwala sprawdzić poprawność wpisanej przez użytkownika liczby rzymskiej (od 1 do 3999)
pattern = r"^M{0,3}(CM|CD|D?C{0,3})" \
          r"(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"

def roman2int(roman: str) -> int:
    total = 0
    prev_value = 0

    if not re.match(pattern, roman): # sprawdzenie poprawności liczby rzymskiej
        raise ValueError(f"{roman} nie jest poprawną liczbą rzymską")
    
    for char in reversed(roman):  # iterujemy od prawej do lewej
        value = roman_dict[char]
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value
    
    return total

# testy funkcji
# print(f"XIV -> {roman2int("XIV")}")  # 14
# print(f"LXX -> {roman2int("LXXX")}")  # 80
# print(f"MCMXCIV -> {roman2int("MCMXCIV")}")  # 1994

assert roman2int("XIV") == 14
assert roman2int("LXXX") == 80
assert roman2int("MCMXCIV") == 1994

user_input = input("Podaj liczbę rzymską do przetłumaczenia na arabską: ")
try:
    result = roman2int(user_input)
    print(f"Liczba w systemie rzymskim zapisywana jako: '{user_input}' to w systemie arabskim: '{result}'.")
except KeyError: # błąd pojawiający się przy próbie dostępu do nieistniejącego klucza w słowniku
    print(f"Wprowadzona wartość '{user_input}' nie jest prawidłową liczbą rzymską.")
except ValueError as ve:
    print(ve)