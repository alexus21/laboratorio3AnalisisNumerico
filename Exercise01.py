import pandas as pd
import numpy as np

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
        dataToView = ["Nombre completo", "Departamento", "Nacionalidad", "Salario"]
        # Nombre, departamento, nacionalidad y sueldo
        print("\nDatos del profesor con más salario:\n")
        print(df.loc[index, dataToView])

        # Filtrar datos
        dataToExport = df.loc[index, dataToView]

        # Exportar a excel
        dataToExport.to_excel("ex01-01-datos-docente-con-mas-ingresos.xlsx", index=False)

    def getTotalAmountPaidToForeigners(self):
        df = self.genDataFrame()

        # Calcular el monto total pagado a profesores extranjeros
        totalForeign = df.loc[df["Nacionalidad"] != "Colombia", "Salario"].sum()
        totalLocal = df.loc[df["Nacionalidad"] == "Colombia", "Salario"].sum()
        percentage = (totalForeign / df["Salario"].sum()) * 100

        # Crear una gráfica de barras que compare los pagos a extranjeros y locales
        labels = ["Extranjeros", "Locales"]
        values = [totalForeign, totalLocal]

        modules.graphics.createBarGraphic(labels, values)

        print("\n")
        print("Total pagado a extranjeros: $", totalForeign)
        print("Porcentaje respecto al total erogado: ", round(percentage, 2), "%")

        dataToExport = pd.DataFrame({"Tipo": ["Extranjeros", "Locales"], "Monto Total Pagado": [totalForeign, totalLocal]})
        dataToExport.to_excel("ex01-02-data-extranjeros.xlsx", index=False)

    def getHighestSpendingDepartment(self):
        df = self.genDataFrame()
        highest_salary_department = df.groupby("Departamento")["Salario"].sum().idxmax()
        print("\n")
        print("Departamento con más ingresos en salarios durante el año:", highest_salary_department)
        totalDepPayments = df.groupby("Departamento")["Salario"].sum()

        # Crear nuevo df para los datos requeridos
        department_data = pd.DataFrame(
            {"Departamento": totalDepPayments.index, "Total Pagado": totalDepPayments.values})

        # Exportar
        department_data.to_excel("ex01-03-departamento-con-mas-egresos.xlsx", index=False)

        # Dibujar la gráfica
        modules.graphics.createTotalPaymentsGraphic(totalDepPayments)


def ex01():
    e = Barranquilla()
    e.genAll()

    continueAction = "y"

    while continueAction == "y":
        print("1. Datos profesor con mas salario")
        print("2. Datos ingresos de profesores extranjeros")
        print("3. Departamento con mas egresos")
        option = int(input("Seleccione una opción: "))

        if option == 1:
            e.getDataHighestEarningTeacher()

        if option == 2:
            e.getTotalAmountPaidToForeigners()

        if option == 3:
            e.getHighestSpendingDepartment()

        else:
            print("Opción inválida")

        continueAction = input("Desea continuar? [y/n]: ")
