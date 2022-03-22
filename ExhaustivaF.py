
from FunExhaus import *
import numpy as np


def exhaustiva(i, dec, k, cos, p):
    pos = 0
    aux = []
    pol = []
    ot = []

    for a in range(i):
        aux.append(-1)

    polipo = politicas(dec, pos, aux, pol, k, ot)

    print("Politicas posibles")
    print(polipo)
    print("\n")

    matrices = []

    for a in range(len(polipo)):
        m = crearmatriz(polipo, a, p)
        m = np.array(m)
        matrices.append(m)

    matrices = np.array(matrices)
    t = len(matrices[0])  # Obtener el tamaño de las matrices
    vector = []  # Vector que añadimos a las matrices
    vecsys = []  # Vector que se usa en el sistema
    for s in range(t):
        vector.append(1)
        vecsys.append(0)

    vecsys[t - 1] = 1
    vecsys = np.array(vecsys)

    mat2 = []
    for s, c in enumerate(matrices):
        matrices[s] = matrices[s].transpose()
        matrices[s] = ajuste(matrices[s])
        matrices[s] = ajuste2(matrices[s])
        mat = quitar(matrices[s])
        mat = np.array(mat)
        mat2.append(mat)
        matrices[s] = insertarfila(mat2[s], vector)

    M = ajustecostos(cos, i, dec, k)

    solsistema = []
    solfinal = []
    cososselec = []
    for s, c in enumerate(matrices):
        sys = sistema2(matrices[s], vecsys)
        if len(sys) == 0:
            pass
        else:
            solsistema.append(sys)
            cosos = solucioncos(M, i, pol[s])
            cososselec.append(cosos)
            resul = sum(np.multiply(solsistema[s], cososselec[s]))
            resul = round(resul, 3)
            solfinal.append(resul)

    print("Costos encontrados")
    print(solfinal)
    print("\n")

    optimo = min(solfinal)
    posoptima = solfinal.index(min(solfinal))
    poloptima = polipo[posoptima]

    print(f"El optimo es: {optimo} ")
    print(f"La politica optima es: {poloptima} ")

    print("\n")
