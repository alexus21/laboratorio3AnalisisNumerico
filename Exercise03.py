import pandas as pd
import numpy as np

# Custom module
from modules.graphics import pieGraphics, barGraphicsEx03


class Hospital:
    def __init__(self):
        self._names = []
        self._age = []
        self._sex = []
        self._condition = []
        self._address = []
        self._phone = []

    def genNameList(self):
        self._names = [
            "Lucas Martínez",
            "Valeria Sánchez",
            "Diego López",
            "Carolina Rodríguez",
            "Juan García",
            "Sofia Fernández",
            "Andrés Ramirez",
            "Laura Torres",
            "Sebastián Herrera",
            "Gabriela Ortiz"
        ]

    def genAgeList(self):
        for i in range(10):
            self._age.append(np.random.randint(7, 85))

    def genSexList(self):
        sexList = ["M", "F"]

        for i in range(10):
            self._sex.append(np.random.choice(sexList))

    def genConditionList(self):
        conditionList = ["1", "2", "3", "4", "5"]

        for i in range(10):
            self._condition.append(np.random.choice(conditionList))


    def genAddress(self):

        addressList = {
            "Calle": [],
            "Numero": [],
            "Colonia": [],
            "Codigo postal": [],
            "Ciudad": []
        }

        streets = [
            "Calle Principal",
            "Avenida de la Libertad",
            "Paseo del Sol",
            "Callejón de los Suspiros",
            "Avenida Central",
            "Calle de la Paz",
            "Avenida de la Victoria",
            "Calle del Sol Naciente",
            "Paseo de la Rosa",
            "Callejón de la Luna"
        ]

        numbers = np.random.randint(1, 1000)

        colonies = [
            "Colonia Juárez",
            "Colonia Roma",
            "Colonia Condesa",
            "Colonia Polanco",
            "Colonia Del Valle",
            "Colonia Narvarte",
            "Colonia Santa Fe",
            "Colonia Cuauhtémoc",
            "Colonia San Ángel",
            "Colonia Lindavista"
        ]

        postCodes = [
            "01000",
            "06100",
            "11420",
            "28010",
            "03100",
            "03020",
            "05300",
            "06500",
            "01060",
            "07300"
        ]

        cities = [
            "Nueva York",
            "Londres",
            "París",
            "Tokio",
            "Sídney",
            "Roma",
            "Moscú",
            "Toronto",
            "Dubái",
            "Ciudad de México"
        ]

        for i in range(10):
            addressList["Calle"].append(np.random.choice(streets))
            addressList["Numero"].append(numbers)
            addressList["Colonia"].append(np.random.choice(colonies))
            addressList["Codigo postal"].append(np.random.choice(postCodes))
            addressList["Ciudad"].append(np.random.choice(cities))

            self._address.append(addressList)

    def genPhoneNumbers(self):
        for i in range(10):
            self._phone.append(np.random.randint(60000000, 79999999))

    def genDataFrame(self):
        dataDict = {
            "Nombre": self._names,
            "Edad": self._age,
            "Sexo": self._sex,
            "Condicion": self._condition,
            "Domicilio": self._address,
            "Telefono": self._phone
        }

        return pd.DataFrame(dataDict)

    def viewPercentagesBySex(self):
        df = self.genDataFrame()
        men = df[df["Sexo"] == "M"].count()["Sexo"]
        women = df[df["Sexo"] == "F"].count()["Sexo"]
        total = men + women
        pieGraphics(men, women, total)

        data = {
            "Sexo": ["Hombres", "Mujeres", "Total"],
            "Cantidad": [men, women, total]
        }
        result_df = pd.DataFrame(data)

        # Exportar el DataFrame a un archivo Excel
        result_df.to_excel("ex03-01-porcentajes-hombres-mujeres.xlsx", index=False)

    def quantityByConditions(self):
        df = self.genDataFrame()
        nConditions = df["Condicion"].value_counts()
        barGraphicsEx03(nConditions)

        # Crear un nuevo DataFrame
        result_df = pd.DataFrame(nConditions)

        # Exportar el DataFrame a un archivo Excel
        result_df.to_excel("ex03-02-condiciones/por-paciente.xlsx", index=False)

    def getDataOfHighConditions(self):
        df = self.genDataFrame()
        maxGravityDetected = df[df["Condicion"] == "5"]
        collectedNames = maxGravityDetected["Nombre"]
        collectedPhones = maxGravityDetected["Telefono"]

        if maxGravityDetected.empty:
            print("No hay pacientes con condición crítica")

        else:
            # Filtrar datos requeridos
            data = {
                "Nombre": collectedNames,
                "Telefono": collectedPhones
            }
            dataToExport = pd.DataFrame(data)

            # Exportar el DataFrame a un archivo Excel
            dataToExport.to_excel("ex03-03-datos_condicion_critica.xlsx", index=False)

            print("Datos de pacientes con condición crítica (5)")
            for name, phone in zip(collectedNames, collectedPhones):
                print(f"Nombre: {name}, Teléfono: {phone}")

    def genAll(self):
        self.genNameList()
        self.genAgeList()
        self.genSexList()
        self.genConditionList()
        self.genAddress()
        self.genPhoneNumbers()


def ex03():
    h = Hospital()
    h.genAll()

    continueAction = "y"

    while continueAction == "y":
        print("1. Porcentaje de hombres y mujeres ingresados")
        print("2. Gráfico de condiciones")
        print("3. Pacientes en condición grave")
        option = int(input("Seleccione una opción: "))

        if option == 1:
            h.viewPercentagesBySex()

        if option == 2:
            h.quantityByConditions()

        if option == 3:
            h.getDataOfHighConditions()

        else:
            print("Opción inválida")

        continueAction = input("Desea continuar? [y/n]: ")

