
from funciones1 import *
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


def iteracion(cos, p, minimo, dec):
    mun = []
    for e in range(i):
        mun.append([])
        for u in range(len(cos[e])):
            f = dec[e][u]
            cu = cos[e][u] + alfa * (sum(np.multiply(p[f-1][e], minimo)))
            mun[e].append(cu)
    return mun


k = int(input("Numero de decisiones: "))
i = int(input("Numero de estados : "))
alfa = float(input("Introducir descuento: "))
n = int(input("Indicar numero de iteraciones: "))
j = i

p = relleno(k, i, j)
dec = decision(i)
cos = costos(dec)

print(dec)

#Solucion inicial
minimo, ind = encontrarMinyPos(cos)
solucion = encontrarsolucion(i, dec, ind)
print("Solucion inicial")
print(solucion)
print("\n")

#Soluciones
for z in range(n-1):
    mun = iteracion(cos, p, minimo, dec)
    print(mun)
    minimo, ind = encontrarMinyPos(mun)
    print(ind)
    solucion = encontrarsolucion(i, dec, ind)
    print(f"Nueva Politica: {solucion}\n")

print(f"La politica optima es: {solucion}\n")
