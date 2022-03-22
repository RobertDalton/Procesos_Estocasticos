
from funciones1 import *


def politicas(lista, pos, so, pol, k , ot):
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


def crearmatriz(polipo, a):
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


def quitar (m):
    m = np.delete(m, len(m)-1, 0)
    return m


def sistema(m, vectorsys):
    system = np.linalg.solve(m, vectorsys)
    return system


def sistema2(m , vectorsys):
    m = np.array(m)
    vectorsys = np.array(vectorsys)
    if (np.linalg.det(m) == 0):
        r = []
    else:
        r = np.dot(np.linalg.inv(m), vectorsys).round(decimals=2)
    r = np.array(r)
    return r


def ajustecostos(cos,i, dec, k):
    m = np.zeros(shape=(i, k))

    for x in range(i):
        for y in range(len(cos[x])):
            a = cos[x][y]
            z = dec[x][y]
            m[x][z-1] = a

    return m


def solucioncos (M, i , pol):
    solve = []
    for s in range(i):
        l = pol[s]
        costo_s = M[s][l-1]
        solve.append(costo_s)
    return solve


k = int(input("Numero de decisiones: "))
i = int(input("Numero de estados : "))
j = i

p = relleno(k, i, j)
dec = decision(i)
cos = costos(dec)

pos = 0
aux = []
pol = []
ot = []

for a in range(i):
    aux.append(-1)

polipo = politicas(dec, pos, aux, pol, k, ot)

print("Politicas posibles")
print(polipo)

matrices = []

for a in range(len(polipo)):
    m = crearmatriz(polipo, a)
    m = np.array(m)
    matrices.append(m)

matrices = np.array(matrices)
t = len(matrices[0]) #Obtener el tamaño de las matrices
vector = [] #Vector que añadimos a las matrices
vecsys = [] #Vector que se usa en el sistema
for s in range(t):
    vector.append(1)
    vecsys.append(0)

vecsys[t-1] = 1
vecsys = np.array(vecsys)

matriginal = matrices

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

print("Costos esperados")
print(solfinal)

optimo = min(solfinal)
posoptima = solfinal.index(min(solfinal))
poloptima = polipo[posoptima]

print(f"El optimo es: {optimo} ")
print(f"La politica optima es: {poloptima} ")

