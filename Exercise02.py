import pandas as pd
import numpy as np


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
        self._employeeFullName = [
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
            self._yearlySales.append(np.random.randint(100000, 9999999))

    def generateMonthlySalary(self):
        for i in range(10):
            self._monthlySalary.append(np.random.randint(500, 1500))

    def generatePaymentMethods(self):
        paymentFormList = ["Efectivo", "Bitcoin", "Crédito", "Débito", "Cheques", "Transferencia"]

        for i in range(10):
            self._paymentForm.append(np.random.choice(paymentFormList))

    def generateBankNames(self):
        paymentFormList = ["BBVA Bancomer, S.A", "Banco Santander", "BBVA Bancomer", "Banco de los Trabajadores", "Banco Hipotecario", "Banco Azteca."]

        for i in range(10):
            self._paymentForm.append(np.random.choice(paymentFormList))

    def generatePaymentKeys(self):
        for i in range(10):
            self._paymentKey.append(np.random.randint(1, 6))

    def getTotalSalesByEmployee(self):
        pass

    def incrementSalary(self):
        pass

    def genAll(self):
        self.generateEmployeeCodes()
        self.generateEmployeesNames()
        self.generateYearlySales()
        self.generateMonthlySalary()
        self.generatePaymentMethods()
        self.generatePaymentKeys()


def ex02():
    e = Empresa()
    e.genAll()

    continueAction = "y"

    while continueAction == "y":
        print("1. Datos profesor con mas salario")
        print("2. Datos ingresos de profesores extranjeros")
        print("3. Departamento con mas egresos")
        option = int(input("Seleccione una opción: "))

        # if option == 1:
        #     e.getDataHighestEarningTeacher()
        #
        # if option == 2:
        #     e.getTotalAmountPaidToForeigners()
        #
        # if option == 3:
        #     e.getHighestSpendingDepartment()
        #
        # else:
        #     print("Opción inválida")

        continueAction = input("Desea continuar? [y/n]: ")
