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


def pieGraphics(men, women, total):
    menPercentage = (men / total) * 100
    womenPercentage = (women / total) * 100

    # Etiquetas y porcentajes
    labels = ['Hombres\n{}'.format(menPercentage), 'Mujeres\n{}'.format(womenPercentage)]
    sizes = [menPercentage, womenPercentage]
    colours = ["#ff9999", "#66b3ff"]

    # Crear la gráfica de pastel
    plt.pie(sizes,
            labels=labels,
            colors=colours,
            autopct='%1.1f%%',
            startangle=90
    )

    # Título
    plt.title("Porcentaje de Hombres y Mujeres Registrados")

    # Mostrar la gráfica
    plt.show()


def barGraphicsEx03(condition):
    plt.bar(condition.index, condition.values)
    plt.xlabel("Condición")
    plt.ylabel("Cantidad de pacientes")
    plt.title("Cantidad de pacientes por condición")
    plt.grid()
    plt.show()
