import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Custom module
import modules.graphics

class Barranquilla:
    def __init__(self):
        self._employeeNumber = []
        self._employeeFullName = []
        self._employeeDepartment = []
        self._employeePost = []
        self._academicLevel = []
        self._nationality = []
        self._salary = []

    def generateEmployeeCodes(self):
        for i in range(10):
            self._employeeNumber.append(np.random.randint(100000, 999999))

    def generateEmployeesNames(self):
        self._employeeFullName = [
            "John Smith",
            "Emily Johnson",
            "Michael Williams",
            "Sophia Brown",
            "Christopher Jones",
            "Olivia Davis",
            "William Miller",
            "Ava Wilson",
            "James Anderson",
            "Isabella Martinez"
        ]

    def generateDepartments(self):
        depsList = ["Matemáticas", "Física", "Ingeniería", "Medicina", "Biología", "Química"]

        for i in range(10):
            self._employeeDepartment.append(np.random.choice(depsList))

    def generatePosts(self):
        postsList = ["Docente", "Pasante", "Investigador", "Coordinador", "Asesor", "Tutor"]

        for i in range(10):
            self._employeePost.append(np.random.choice(postsList))

    def generateAcademicLevel(self):
        levelsList = ["Ingeniero", "Licenciado", "Máster", "Doctor"]

        for i in range(10):
            self._academicLevel.append(np.random.choice(levelsList))

    def generateNationalities(self):
        nationalitiesList = ["Argentina", "Colombia", "El Salvador", "Alemania", "Estados Unidos"]

        for i in range(10):
            self._nationality.append(np.random.choice(nationalitiesList))

    def generateRandomSalary(self):
        for i in range(10):
            self._salary.append(np.random.randint(800, 5000))

    def genDataFrame(self):
        dataDict = {
            "Número": self._employeeNumber,
            "Nombre completo": self._employeeFullName,
            "Departamento": self._employeeDepartment,
            "Puesto": self._employeePost,
            "Nivel académico": self._academicLevel,
            "Nacionalidad": self._nationality,
            "Salario": self._salary
        }

        return pd.DataFrame(dataDict)

    def genAll(self):
        self.generateEmployeeCodes()
        self.generateEmployeesNames()
        self.generateDepartments()
        self.generatePosts()
        self.generateAcademicLevel()
        self.generateNationalities()
        self.generateRandomSalary()

    def getDataHighestEarningTeacher(self):
        df = self.genDataFrame()
        index = df["Salario"].idxmax()
        # Nombre, departamento, nacionalidad y sueldo
        print("Datos del profesor con más salario:\n")
        print(df.loc[index, ["Nombre completo", "Departamento", "Nacionalidad", "Salario"]])

    def getTotalAmountPaidToForeigners(self):
        df = self.genDataFrame()

        # Calcular el monto total pagado a profesores extranjeros
        totalForeign = df.loc[df["Nacionalidad"] != "Colombia", "Salario"].sum()
        totalLocal = df.loc[df["Nacionalidad"] == "Colombia", "Salario"].sum()
        percentage = (totalForeign / df["Salario"].sum())*100

        # Crear una gráfica de barras que compare los pagos a extranjeros y locales
        labels = ["Extranjeros", "Locales"]
        values = [totalForeign, totalLocal]

        modules.graphics.createBarGraphic(labels, values)
        print("\n")
        print("Total pagado a extranjeros: $", totalForeign)
        print("Porcentaje respecto al total erogado: ", round(percentage, 2), "%")

    def getHighestSpendingDepartment(self):
        df = self.genDataFrame()

        # Obtener el año actual
        current_year = pd.Timestamp.now().year

        # Filtrar los datos por el año actual
        df_current_year = df[df.index.year == current_year]

        # Calcular el total de ingresos por departamento
        department_incomes = df_current_year.groupby("Departamento")["Salario"].sum()

        # Obtener el departamento con el mayor total de ingresos
        highest_income_department = department_incomes.idxmax()

        print("Departamento con más ingresos en salarios durante el año:", highest_income_department)


def ex01():
    e = Barranquilla()
    e.genAll()
    e.getDataHighestEarningTeacher()
    e.getTotalAmountPaidToForeigners()
    # e.getHighestSpendingDepartment()

ex01()
