# Ulloa Serpas, Hugo Alexander
# US21003

from Exercise01 import ex01


def main():
    continueAction = "y"

    while continueAction == "y":
        print("1. Ejercicio #1")
        print("2. Ejercicio #2")
        print("3. Ejerciccio #3")
        option = int(input("Seleccione una opción: "))

        if option == 1:
            ex01()

        # if option == 2:
        #     e.getTotalAmountPaidToForeigners()
        #
        # if option == 3:
        #     e.getHighestSpendingDepartment()

        else:
            print("Opción inválida")

        continueAction = input("Desea ver otro ejercicio? [y/n]: ")


if __name__ == "__main__":
    main()
