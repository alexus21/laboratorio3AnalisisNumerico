import pandas as pd
import numpy as np

from modules.graphics import lineGraphics

class Empresa:
    def __init__(self):
        self._vendorNumber = []
        self._vendorFullName = []
        self._yearlySales = []
        self._monthlySalary = []
        self._paymentKey = []
        self._paymentForm = []
        self._bankName = []

    def generateEmployeeCodes(self):
        for i in range(10):
            self._vendorNumber.append(np.random.randint(100000, 999999))

    def generateEmployeesNames(self):
        self._vendorFullName = [
            "Barbara Bolaños",
            "Josue Navarro",
            "Ursula Perales",
            "Mercedes Arce",
            "Sergio Checa",
            "Angela-Maria Torregrosa",
            "Enrique Acuña",
            "Jose Andres Pareja",
            "Alexandra Gaspar",
            "Bartolome Pulido"
        ]

    def generateYearlySales(self):
        for i in range(10):
            self._yearlySales.append(np.random.randint(500000, 9999999))

    def generateMonthlySalary(self):
        for i in range(10):
            self._monthlySalary.append(np.random.randint(500, 1500))

    def generatePaymentKeys(self):
        for i in range(10):
            self._paymentKey.append(np.random.randint(1, 6))

    def generatePaymentMethods(self):
        paymentFormList = ["Efectivo", "Bitcoin", "Crédito", "Débito", "Cheques", "Transferencia"]

        for i in range(10):
            self._paymentForm.append(np.random.choice(paymentFormList))

    def generateBankNames(self):
        bankNameList = ["BBVA Bancomer, S.A", "Banco Santander", "BBVA Bancomer", "Banco de los Trabajadores",
                        "Banco Hipotecario", "Banco Azteca."]

        for i in range(10):
            self._bankName.append(np.random.choice(bankNameList))

    def genDataDict(self):
        dataDict = {
            "Código": self._vendorNumber,
            "Nombre completo": self._vendorFullName,
            "Ventas anuales": self._yearlySales,
            "Salario mensual": self._monthlySalary,
            "Clave de forma de pago": self._paymentKey,
            "Forma de pago": self._paymentForm,
            "Banco: ": self._bankName
        }

        return pd.DataFrame(dataDict)

    def getTotalSalesByEmployee(self):
        df = self.genDataDict()
        totalYearlySales = df["Ventas anuales"].sum()
        print(df[["Código", "Nombre completo", "Ventas anuales"]])
        print("Ventas totales anuales: $", totalYearlySales)

        # Eje x
        employees = range(len(df))

        # Eje y
        yearlySales = df["Ventas anuales"]

        # Gráfica
        lineGraphics(employees, yearlySales)

    def incrementSalary(self):
        df = self.genDataDict()
        print("Salarios actuales: ")
        print(df[["Código", "Nombre completo", "Salario mensual"]])

        incremented = np.where(df["Ventas anuales"] > 1500000,
                                         df["Salario mensual"] * 1.15,
                                         df["Salario mensual"])

        modifiedSalaries = df[df["Salario mensual"] != incremented]
        print("Salarios modificados:")
        print(modifiedSalaries[["Código", "Nombre completo", "Salario mensual"]])

    def genAll(self):
        self.generateEmployeeCodes()
        self.generateEmployeesNames()
        self.generateYearlySales()
        self.generateMonthlySalary()
        self.generatePaymentMethods()
        self.generatePaymentKeys()
        self.generateBankNames()


def ex02():
    e = Empresa()
    e.genAll()

    continueAction = "y"

    while continueAction == "y":
        print("1. Ventas totales anuales")
        print("2. Datos ingresos de profesores extranjeros")
        print("3. Departamento con mas egresos")
        option = int(input("Seleccione una opción: "))

        if option == 1:
            e.getTotalSalesByEmployee()

        if option == 2:
            e.incrementSalary()
        #
        # if option == 3:
        #     e.getHighestSpendingDepartment()
        #
        # else:
        #     print("Opción inválida")

        continueAction = input("Desea continuar? [y/n]: ")


ex02()