import matplotlib.pyplot as plt


def createBarGraphic(labels, values):
    plt.bar(labels, values)
    plt.xlabel("Tipo de profesor")
    plt.ylabel("Monto total de pagos")
    plt.title("Comparación de pagos a profesores extranjeros y locales")
    plt.grid()
    plt.show()


def createTotalPaymentsGraphic(totalDepPayments):
    plt.plot(totalDepPayments.index, totalDepPayments.values)
    plt.xlabel("Departamento")
    plt.ylabel("Total de pagos")
    plt.title("Total de pagos por departamento")
    plt.grid()

    # Add labels to each point
    for x, y in zip(totalDepPayments.index, totalDepPayments.values):
        plt.text(x, y, str(y))

    plt.show()


def lineGraphics(nEmployees, yearlySales):
    plt.plot(nEmployees, yearlySales)
    plt.xlabel("Empleado")
    plt.ylabel("Ventas anuales")
    plt.title("Ventas anuales por empleado")
    plt.grid()

    for i, (x, y) in enumerate(zip(nEmployees, yearlySales)):
        plt.text(x, y, f"${y}")

    plt.show()
