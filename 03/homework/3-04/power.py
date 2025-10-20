#!/usr/bin/env python3
# coding=utf-8

# Napisać program pobierający w pętli od użytkownika liczbę rzeczywistą x (typ float) i wypisujący x oraz trzecią potęgę x.
# Zatrzymanie programu następuje po wpisaniu z klawiatury stop. Jeżeli użytkownik wpisze napis zamiast liczby, to program ma wypisać komunikat o błędzie i kontynuować pracę.

while True:
    user_input = input("Podaj liczbę do spotęgowania lub wpisz 'stop', jeśli program ma zakończyć pracę: ")

    if user_input.lower() == "stop":
        print("Program zakończony przez użytkownika.\n")
        break

    try:
        x = float(user_input)
        print(f"Wpisana liczba to {x},\n{x}^3 to {pow(x, 3)}\n")
    except ValueError:
        print("Wpisana wartość nie jest liczbą, ani napisem 'stop'. Spróbuj ponownie.\n")
