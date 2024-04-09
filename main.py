import numpy as np
from functions import *

print("Podaj ilosc rownan. (Min 2, Max 10)")

poprawna_wartosc = True

while poprawna_wartosc:
    try:
        ilosc_rownan = int(input("Podaj liczbe: "))
        if 2 <= ilosc_rownan <= 10:
            poprawna_wartosc = False
        else:
            print("Niepoprawny wybor wybierz liczbe calkowita 2-10.")
    except ValueError:
        print("Niepoprawny wybor wybierz liczbe calkowita 2-10.")

print("Co chcesz zrobic?\n"
      "1 - pobrac dane z pliku\n"
      "2 - wpisac dane w terminalu\n")

poprawna_wartosc = True

while poprawna_wartosc:
    try:
        wybor_danych = int(input("Podaj cyfre: "))
        poprawna_wartosc = False
    except ValueError:
        print("Niepoprawny wybor wybierz opcje 1 lub 2.")

if wybor_danych == 1:
    lista_glowna = np.genfromtxt("data.txt", delimiter=',').tolist()
    print(lista_glowna)

if wybor_danych == 2:
    lista_glowna = []

    for i in range(ilosc_rownan):
        lista1 = []
        for j in range(ilosc_rownan+1):
            cyfra = float(input(f"Podaj cyfrę dla równania {i+1}, element {j+1}: (Ostatni element to y) "))
            lista1.append(cyfra)
        lista_glowna.append(lista1)
    print(lista_glowna)

gauss(ilosc_rownan, lista_glowna)
