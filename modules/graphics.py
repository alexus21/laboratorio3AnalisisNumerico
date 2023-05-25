import matplotlib.pyplot as plt

def createBarGraphic(labels, values):
    plt.bar(labels, values)
    plt.xlabel("Tipo de profesor")
    plt.ylabel("Monto total de pagos")
    plt.title("Comparación de pagos a profesores extranjeros y locales")
    plt.show()
