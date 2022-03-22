
import numpy as np

def relleno (k, i, j):
    pol3 = []
    for f in range(k):
        print(f"Politica {f + 1}")
        b = [[float(input(f"Probabilidad {c} a {d}: "))
              for c in range(i)] for d in range(j)]
        b = np.array(b)
        b1 = np.transpose(b)
        pol3.append(b1)
    pol3 = np.array(pol3)
    return pol3

def decision (i):
    dec = []
    for i in range(i):
        b = int(input(f"Cuantas decisiones son posibles para el estado {i}: "))
        dec.append([])
        for j in range(b):
            d = int(input(f"Indique Decision: "))
            dec[i].append(d)
    return dec

def costos(dec):
    costos=[]
    for a, ind in enumerate(dec):
        costos.append([])
        for b, indid in enumerate(dec[a]):
            cost = float(input(f"Costo {a}{dec[a][b]}: "))
            costos[a].append(cost)
    return costos

