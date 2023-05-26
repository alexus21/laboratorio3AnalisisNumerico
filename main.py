# Ulloa Serpas, Hugo Alexander
# US21003

from Exercise01 import ex01
from Exercise02 import ex02
from Exercise03 import ex03

def main():
    continueAction = "y"

    while continueAction == "y":
        print("1. Ejercicio #1")
        print("2. Ejercicio #2")
        print("3. Ejerciccio #3")
        print("99. Cancelar")
        option = int(input("Seleccione una opción: "))

        if option == 1:
            ex01()

        if option == 2:
            ex02()


        if option == 3:
            ex03()

        if option == 99:
            exit(0)

        else:
            print("Opción inválida")

        continueAction = input("Desea ver otro ejercicio? [y/n]: ")


if __name__ == "__main__":
    main()
