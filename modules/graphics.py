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
    plt.show()