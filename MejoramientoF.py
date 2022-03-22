
from funmejora import *


def mejoramiento(i, k, p, costos, dec):
    # Esto siempre se hara
    print("INTRODUCIR POLÍTICA INICIAL")
    poli = politica(i)
    print("LA POLITICA RECIBIDA ES:")
    print(poli)
    print("\n")
    print("MATRIZ DE PROBABILIDADES FORMADA POR LA POLÍTICA DADA")
    matriz = nuevamatriz(poli, p)
    print(matriz)

    sistema = algoritmo(matriz, i)

    costo2 = costsistema(poli, dec, i, k, costos)
    print("\n")

    r = solucion(sistema, costo2)
    if len(r) == 0:
        print("Introducir otra politica inicial")

    else:

        while True:
            lis = mejora(costos, p, r, dec, i)
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
                nsistema = algoritmo(nmatriz, i)
                ncosto = costsistema(newpolitic, dec, i, k, costos)
                r = solucion(nsistema, ncosto)
                if len(r) == 0:
                    break
                else:
                    poli = newpolitic

        print(f"LA SOLUCION OPTIMA ES: {newpolitic}\n ")
