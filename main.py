# Ulloa Serpas, Hugo Alexander
# US21003

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Ejercicio 1

class UBarranquilla:
    def __init__(self, data):
        # Collection de datos
        self.df = pd.DataFrame(data)

    def findMaxSalaryInfo(self):
        # Obtener el indice de la fila que contiene el mayor salario registrado
        index = self.df["Salary"].idxmax()

        # Mostrar valores
        print("Resultado obtenidos: \n", self.df.loc[index])

    def findTotalForeignersAmount(self):
        filtering = self.df["Nationality"] != "Colombia"
        filterItems = self.df.loc[filtering]
        print("\nSalarios totales: ", filterItems["Salary"].sum())
        percentage = round((filterItems["Salary"].sum() / self.df["Salary"].sum()) * 100, 2)
        print("Porcentaje: ", percentage, "%")

    def findDepartmentWithMorePayments(self):
        morePayments = self.df.groupby["Department"]("Salary").sum()
        index = morePayments.idmax()

        # Mostrar valores
        # print("Departamento con mas ingresos: \n", self.df.loc[index])
        print("\nSalarios totales: ", index)


def firstExercise():
    dataDict = {"ID": [],
                "Name": [],
                "Departament": [],
                "Position": [],
                "Grade": [],
                "Nationality": [],
                "Salary": []}

    continueOp = 1

    while continueOp == 1:
        employeeNumber = int(input("Numero del empleado: "))

        while employeeNumber <= 0:
            employeeNumber = int(input("Numero del empleado: "))

        fullName = input("Nombre y apellido: ")

        while fullName == "":
            fullName = input("Nombre y apellido: ")

        department = input("Departamento: ")

        while department == "":
            department = input("Departamento: ")

        jobHeld = input("Posición: ")

        while jobHeld == "":
            jobHeld = input("Posición: ")

        academicDegree = input("Grado académico: ")

        while academicDegree == "":
            academicDegree = input("Grado académico: ")

        nationality = input("Nacionalidad: ")

        while nationality == "":
            nationality = input("Nacionalidad: ")

        salary = float(input("Salario: "))

        while salary <= 0:
            salary = float(input("Salario: "))

        dataDict["ID"].append(employeeNumber)
        dataDict["Name"].append(fullName)
        dataDict["Departament"].append(department)
        dataDict["Position"].append(jobHeld)
        dataDict["Grade"].append(academicDegree)
        dataDict["Nationality"].append(nationality)
        dataDict["Salary"].append(salary)

        continueOp = int(input("Para continuar, presione '1'; para salir, cualquier numero \n> "))

    ub = UBarranquilla(dataDict)
    ub.findMaxSalaryInfo()
    ub.findTotalForeignersAmount()


def main():
    firstExercise()


if __name__ == "__main__":
    main()
