

from funciones1 import *
import numpy as np


def multiplicar(h, r):
    for x in range(len(r)):
        r[x] = h*r[x]
    return r

#función para política inicial
def politica(i):
    poli = []
    for f in range(i):
        b = int(input(f"Para el estado {f}: "))
        poli.append(b)
    return poli


#función para la matriz por política
def nuevamatriz (poli):
    matriz = []
    for b in range(len(poli)):
        pos = poli[b]
        ren = p[pos-1][b]
        matriz.append(ren)
    matriz = np.array(matriz)
    return matriz


#función para crear el sistema
def algoritmo(matriz, i, h):
    aux = []
    gRn = []
    for e in range(i):
        for u in range(i):
            if (e == u & u < i-1):
                matriz[e][e] = 1-matriz[e][e]
            else:
                if (matriz[e][u]!=0):
                    matriz[e][u] = -1*matriz[e][u]
                matriz[e][i-1] = 0
        aux = matriz[e]
        gRn.append(aux)
    gRn = multiplicar(h, gRn)
    gRn = np.array(gRn)
    sistema = np.zeros((i, i))
    for e in range(i):
        for u in range(i):
            if (u == 0):
                sistema[e][0] = 1
            else:
                sistema[e][u] = gRn[e][u-1]
    sistema=np.array(sistema)
    return sistema


#función para los costos del sistema
def costsistema (poli, dec, i, k):
    costo2 = []
    aux2 = []
    for e in range(i):
        for u in range(len(dec[e])):
            for a in range(k):
                if (poli[e] == a+1 & a+1 == dec[e][u]):
                    aux2 = costos[e][u]
                    costo2.append(aux2)
    costo2=np.array(costo2)
    return costo2


#función que resuelve el sistema
def solucion (sistema,costo2):
    r = []
    if (np.linalg.det(sistema) == 0):
        r = None
        print("No se puede resolver el sistema")
    else:
        r = np.dot(np.linalg.inv(sistema), costo2).round(decimals=2)
    r = np.array(r)
    return r


#Funcion que hace la mejora
def mejora(cos, p, r, dec, h):
    mun = []
    for e in range(i):
        mun.append([])
        for u in range(len(cos[e])):
            f = dec[e][u]
            cu = cos[e][u] + (h * sum(np.multiply(p[f-1][e], r)))
            mun[e].append(cu)
    return mun


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


k = int(input("Numero de decisiones: "))
i = int(input("Numero de estados : "))
h = float(input("Introducir descuento: "))
j = i

dec = decision(i)

costos = costos(dec)

p = relleno(k, i, j)

#Esto siempre se hara
print("INTRODUCIR POLÍTICA INICIAL")
poli = politica(i)
print("LA POLITICA RECIBIDA ES:")
print(poli)
print("\n")
print("MATRIZ DE PROBABILIDADES FORMADA POR LA POLÍTICA DADA")
matriz = nuevamatriz(poli)
print(matriz)


sistema = algoritmo(matriz, i, h)

costo2 = costsistema(poli, dec, i, k)
print("\n")

r = solucion(sistema, costo2)

while True:
    lis = mejora(costos, p, r, dec, h)
    minimo, ind = encontrarMinyPos(lis)
    newpolitic = encontrarsolucion(i, dec, ind)

    print(f"NUEVA POLITICA: {newpolitic}\n")

    if newpolitic == poli:
        break

    else:
        nmatriz = nuevamatriz(newpolitic)
        print(f"NUEVA MATRIZ DE PROBABILIDADES")
        print(nmatriz)
        print("\n")
        nsistema = algoritmo(nmatriz, i, h)
        ncosto = costsistema(newpolitic, dec, i, k)
        r = solucion(nsistema, ncosto)
        poli = newpolitic

print(f"LA SOLUCION OPTIMA ES: {newpolitic}\n ")
