
from FunAprox import*


def aproximaciones(cos, dec, i, p):

    alfa = float(input("Introducir descuento: "))
    n = int(input("Indicar numero de iteraciones: "))
    minimo, ind = encontrarMinyPos(cos)
    solucion = encontrarsolucion(i, dec, ind)
    print("Solucion inicial")
    print(solucion)

    # Soluciones
    for z in range(n - 1):
        mun = iteracion(cos, p, minimo, alfa, i, dec)
        minimo, ind = encontrarMinyPos(mun)
        solucion = encontrarsolucion(i, dec, ind)
        print(f"Nueva politica: {solucion}\n")

    print(f"La politica optima es: {solucion}\n")
