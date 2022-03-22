
from funciones1 import *


def datos():

    print("Lectura de datos")

    k = int(input("Numero de decisiones: "))
    i = int(input("Numero de estados : "))
    j = i

    p = relleno(k, i, j)
    dec = decision(i)
    cos = costos(dec)

    print("Datos introducidos!\n")

    return p, dec, cos, k, i, j
