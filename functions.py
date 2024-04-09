def gauss(ilosc_rownan, lista_glowna):
    uklad_sprzeczny = uklad_oznaczony = uklad_nieoznaczony = False
    lista2 = []
    iterator = 0

    while not uklad_sprzeczny and not uklad_oznaczony and not uklad_nieoznaczony:
        if iterator < ilosc_rownan - 1:
            czy_same_zera = False
            for wiersz in lista_glowna:
                czy_same_zera = all(round(element, 10) == 0 for element in wiersz)
            if czy_same_zera:
                uklad_nieoznaczony = True
            else:
                for m in range(iterator, ilosc_rownan):
                    lista2.append(lista_glowna[m][iterator])
                index1 = lista2.index(max(lista2))

                for g in range(ilosc_rownan - iterator + 1):
                    lista_glowna[iterator][iterator + g], lista_glowna[iterator + index1][iterator + g] \
                        = lista_glowna[iterator + index1][iterator + g], lista_glowna[iterator][
                        iterator + g]

                for i in range(ilosc_rownan - 2):
                    if lista_glowna[iterator + 1][iterator + 1] == 0:
                        for g in range(ilosc_rownan - iterator):
                            lista_glowna[iterator + 1][iterator + 1 + g], lista_glowna[iterator + 2][iterator + 1 + g] \
                                = lista_glowna[iterator + 2][iterator + 1 + g], lista_glowna[iterator + 1][
                                iterator + 1 + g]

                lista2 = []
                for a in range(ilosc_rownan):
                    if round(lista_glowna[a][a], 10) == 0:
                        uklad_sprzeczny = True
                if not uklad_sprzeczny:
                    for i in range(iterator + 1, ilosc_rownan):
                        wspolczynnik = lista_glowna[i][iterator] / lista_glowna[iterator][iterator]
                        for j in range(iterator, ilosc_rownan + 1):
                            lista_glowna[i][j] -= wspolczynnik * lista_glowna[iterator][j]
            iterator += 1
        else:
            czy_same_zera = False
            for wiersz in lista_glowna:
                czy_same_zera = all(round(element, 10) == 0 for element in wiersz)
            if czy_same_zera:
                uklad_nieoznaczony = True
                print("Uklad jest nieoznaczony.")
            if not uklad_nieoznaczony:
                for a in range(ilosc_rownan):
                    if round(lista_glowna[a][a], 10) == 0:
                        uklad_sprzeczny = True
                if not uklad_sprzeczny:
                    uklad_oznaczony = True

    if uklad_sprzeczny:
        print("Uklad jest sprzeczny.")

    if uklad_oznaczony:
        print("Znaleziono rozwiazanie:")
        solution = podstawianie_w_tyl(lista_glowna)
        for i, val in enumerate(solution):
            if round(val, 5) == 0:
                print(f"x{i + 1} = {0.0}")
            else:
                print(f"x{i + 1} = {round(val, 1)}")


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
