
from Datos import *
from AproximacionesF import *
from ExhaustivaF import *
from MejoramientoF import *
from MejoramientoDF import *

p, dec, cos, k, i, j = datos()

while True:
    print("\tAlgoritmos")
    print("1. Enumeracion Exhaustiva: ")
    print("2. Aproximaciones Sucesivas: ")
    print("3. Mejoramiento de Politicas: ")
    print("4. Mejoramiento de Politicas con Descuento: ")
    print("5. Salir")
    opcion = int(input("Digite una opcion del menu: "))

    print("\n")

    if opcion == 1:
        print("Enumeracion Exhaustiva\n")
        exhaustiva(i, dec, k, cos, p)
        print("\n")

    elif opcion == 2:
        print("Aproximaciones Sucesivas\n")
        aproximaciones(cos, dec, i, p)
        print("\n")

    elif opcion == 3:
        print("Mejoramiento de Politicas\n")
        mejoramiento(i, k, p, cos, dec)
        print("\n")

    elif opcion == 4:
        print("Mejoramiento de Politicas con Descuento\n")
        mejoramientod(i, k, dec, p, cos)
        print("\n")

    elif opcion == 5:
        break

    else:
        print("Opcion no valida")
        print("\n")
