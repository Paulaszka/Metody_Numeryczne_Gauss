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