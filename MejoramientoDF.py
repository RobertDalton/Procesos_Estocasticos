
from funmejorad import *


def mejoramientod(i, k, dec, p, costos):
    # Esto siempre se hara
    h = float(input("INTRODUCIR DESCUENTO: "))
    print("INTRODUCIR POLÍTICA INICIAL")
    poli = politica(i)
    print("LA POLITICA RECIBIDA ES:")
    print(poli)
    print("\n")
    print("MATRIZ DE PROBABILIDADES FORMADA POR LA POLÍTICA DADA")
    matriz = nuevamatriz(poli, p)
    print(matriz)

    sistema = algoritmo(matriz, i, h)

    costo2 = costsistema(poli, dec, i, k, costos)
    print("\n")

    r = solucion(sistema, costo2)
    if len(r) == 0:
        print("Introduzca otra politica inicial: ")
    else:

        while True:
            lis = mejora(costos, p, r, dec, h, i)
            minimo, ind = encontrarMinyPos(lis)
            newpolitic = encontrarsolucion(i, dec, ind)

            print(f"NUEVA POLITICA: {newpolitic}\n")

            if newpolitic == poli:
                break

            else:
                nmatriz = nuevamatriz(newpolitic, p)
                print(f"NUEVA MATRIZ DE PROBABILIDADES")
                print(nmatriz)
                print("\n")
                nsistema = algoritmo(nmatriz, i, h)
                ncosto = costsistema(newpolitic, dec, i, k, costos)
                r = solucion(nsistema, ncosto)
                if len(r) == 0:
                    break
                else:
                    poli = newpolitic

        print(f"LA SOLUCION OPTIMA ES: {newpolitic}\n ")
