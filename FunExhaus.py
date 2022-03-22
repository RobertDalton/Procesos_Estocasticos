import numpy as np


def politicas(lista, pos, so, pol, k, ot):
    if pos != len(lista):
        for a in range(1, k+1):
            if a in lista[pos]:
                so[pos] = a
                ot = [num for num in so]
                politicas(lista, pos + 1, so, pol, k, ot)
            else:
                pass

    else:
        pol.append(ot)
    return pol


def crearmatriz(polipo, a, p):
    matriz = []
    for b in range(len(polipo[a])):
        pos = polipo[a][b]
        ren = p[pos-1][b]
        matriz.append(ren)
    return matriz


def ajuste(m):
    for a, c in enumerate(m):
        for b, d in enumerate(m):
            m[a][b] = m[a][b]*-1
    return m


def ajuste2(m):
    for a, c in enumerate(m):
        for b, d in enumerate(m):
            if a == b:
                m[a][b] = m[a][b]+1
            else:
                pass
    return m


def insertarfila(m, vector):
   m = np.vstack((m, vector))

   return m


def quitar(m):
    m = np.delete(m, len(m)-1, 0)
    return m


def sistema(m, vectorsys):
    system = np.linalg.solve(m, vectorsys)
    return system


def ajustecostos(cos, i, dec, k):
    m = np.zeros(shape=(i, k))

    for x in range(i):
        for y in range(len(cos[x])):
            a = cos[x][y]
            z = dec[x][y]
            m[x][z-1] = a

    return m


def solucioncos (M, i, pol):
    solve = []
    for s in range(i):
        l = pol[s]
        costo_s = M[s][l-1]
        solve.append(costo_s)
    return solve


def sistema2(m, vectorsys):
    m = np.array(m)
    vectorsys = np.array(vectorsys)
    if (np.linalg.det(m) == 0):
        r = []
    else:
        r = np.dot(np.linalg.inv(m), vectorsys).round(decimals=2)
    r = np.array(r)
    return r
