import csv

Namefile = "mimosa.csv"


def write():
    # Datos para crear el CSV 🤫
    # field names
    fields = ["Name", "Surname", "Age"]

    # datos para reyenar los fields
    data = [["Milanes", "Greco Romano", "34"],
            ["Mago", "de Oz", "124"],
            ["Bad", "Bunny YHQMDLG", "23"],
            ["San Lucas", "De la fuente", "19"],
            ["Pikachu", "Picachorizo Lvl20", "10"],
            ["Charizard", "Chorizord Lvl20", "18"]]

    # Escribe el archivo y
    # Crea el Archivo CSV 😏
    with open("mimosa.csv", 'w') as csvfile:
        # Crea el archivo
        csvwriter = csv.writer(csvfile)

        # Escribe el fichero los fields
        csvwriter.writerow(fields)

        # Escribe el fichero los datos
        csvwriter.writerows(data)


def read():
    # Abre el CSV 😎
    with open("mimosa.csv", 'r') as file:
        # Lee el CSV 🥵
        csvFile = csv.reader(file)

        # Muestra el CSV 🤓
        for lines in csvFile:
            print(lines)


write()
read()
