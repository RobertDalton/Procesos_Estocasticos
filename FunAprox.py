
import numpy as np


def encontrarMinyPos(lista):
    ind = []
    minimo = []
    for x, indic in enumerate(lista):
        ks = min(lista[x])
        kd = lista[x].index(min(lista[x]))
        ind.append(kd)
        minimo.append(ks)

    return minimo, ind


def encontrarsolucion(i, dec, ind):
    sol = []
    for x in range(i):
        pos = ind[x]
        s = dec[x][pos]
        sol.append(s)
    return sol


def iteracion(cos, p, minimo, alfa, i, dec):
    mun = []
    for e in range(i):
        mun.append([])
        for u in range(len(cos[e])):
            f = dec[e][u]
            cu = cos[e][u] + alfa * (sum(np.multiply(p[f-1][e], minimo)))
            mun[e].append(cu)
    return mun
