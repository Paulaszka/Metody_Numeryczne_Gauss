import numpy as np


def wyswietl_macierz(macierz):
    for wiersz1 in macierz:
        for element in wiersz1:
            print(round(element, 4), end=" ")
        print()


def podstawianie_w_tyl(macierz):
    n = len(macierz)
    x = [0] * n

    for t in range(n - 1, -1, -1):
        x[t] = macierz[t][n] / macierz[t][t]

        for p in range(t - 1, -1, -1):
            macierz[p][n] -= macierz[p][t] * x[t]
    return x


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


uklad_sprzeczny = uklad_oznaczony = uklad_nieoznaczony = False
lista2 = []
lista3 = []
iterator = 0

while not uklad_sprzeczny and not uklad_oznaczony and not uklad_nieoznaczony:
    if iterator < ilosc_rownan:
        if lista_glowna[iterator][iterator] != 0:
            for wiersz in lista_glowna:
                czy_same_zera = all(element == 0 for element in wiersz)
                if czy_same_zera:
                    uklad_nieoznaczony = True
                    print("Znaleziono nieskonczone rozwiazania")
                    print(lista_glowna)
                else:
                    for m in range(ilosc_rownan):
                        lista2.append(lista_glowna[iterator][m])
                    index1 = lista2.index(max(lista2))
                    lista3.append(lista_glowna[iterator])
                    for g in range(ilosc_rownan+1):
                        lista_glowna[iterator][g] = lista_glowna[index1][g]
                        lista_glowna[index1][g] = lista3[g]

                    for k in range(ilosc_rownan-1):
                        for i in range(k+1, ilosc_rownan):
                            wspolczynnik = lista_glowna[i][k] / lista_glowna[k][k]
                            for j in range(k, ilosc_rownan+1):
                                lista_glowna[i][j] -= wspolczynnik * lista_glowna[k][j]
                                iterator += 1
        else:
            uklad_sprzeczny = True
            print("Uklad jest sprzeczny")
            print(lista_glowna)
    else:
        uklad_oznaczony = True
        print("Znaleziono rozwiazanie")
        print(lista_glowna)

if uklad_oznaczony:
    solution = podstawianie_w_tyl(lista_glowna)
    print("Rozwiązanie:")
    for i, val in enumerate(solution):
        print(f"x{i+1} = {val}")

wyswietl_macierz(lista_glowna)
