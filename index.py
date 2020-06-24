from prettytable import PrettyTable
import math
import os
import json

field_names = ["Estrela", "Tipo", "Temp. (K)", f"Lum. (○)", f"Massa (M○)", "Comp. de Onda (μm)",
               f"Raio (R○)", "Mag. Aparente", "Mag. Absoluta", "Dist (LY)", "K"]

sortField = "Estrela"


def createTable():
    table = PrettyTable()
    table.field_names = field_names
    table.sortby = sortField
    return table


def loginStar():
    star = []
    star.append(str(input("Nome da Estrela: ")))  # 0
    star.append(str(input("Tipo: ")))  # 1
    star.append(float(input("Temperatura em Kelvin: ")))  # 2
    star.append(float(input("Luminosidade em ○: ")))  # 3
    star.append(float(input("Massa em ○: ")))  # 4
    star.append(round(waveLength(star[2]), 2))  # 5
    star.append(float(input("Raio em ○: ")))  # 6
    star.append(float(input("Magnitude Aparente: ")))  # 7
    star.append(float(input("Magnitude Absoluta: ")))  # 8
    star.append(float(input("Distância em LY: ")))  # 9

    os.system("cls")

    L = star[3] * (3.9*(10**26))
    r = 3 * 10**17
    F = L/(4 * math.pi * (r**2))
    k = star[8] + 2.5 * math.log10(F)

    star.append(round(k, 2))

    return star


def readJson():
    with open("database.json", "r") as file:
        data = json.load(file)
    return data


def writeJson(stars):
    with open("database.json", "w") as file:
        json.dump(stars, file, indent=5)


def resetJson():
    file = open("database.json", "w")
    file.write("[]")
    file.close()


def waveLength(T):
    return 2860/T


while True:
    table = createTable()
    stars = readJson()
    for star in stars:
        table.add_row(star)

    print()
    print(table)
    print()
    print(f"Parâmetro: {sortField}")
    print()
    print("[A] - Add Estrela || [R] - Remover Estrela || [Q] - Sair || [RESET] - Resetar Estrelas || [O] - Ordenar Estrelas")
    option = str(input("O que deseja fazer: "))
    option = option.lower()
    option = option.split(" ")

    if option[0] == "a":
        newStar = loginStar()
        stars.append(newStar)
        writeJson(stars)
        table.add_row(newStar)
        os.system("cls")

    if option[0] == "r":
        name = str(input("Nome da Estrela: ")).lower()
        for star in stars:
            if star[0].lower() == name:
                del(stars[stars.index(star)])
                writeJson(stars)
        os.system("cls")

    elif option[0] == "reset":
        if "confirmar" == str(input("Escreva (confirmar)")).lower():
            resetJson()
        os.system("cls")

    elif option[0] == "o":
        print("Digite o número da característica")
        print()
        for name in field_names:
            print(f"{field_names.index(name)} - {name}")
        sortField = table.field_names[int(
            input(f"Número do campo: 0 <-> {len(field_names) - 1}: "))]
        os.system("cls")

    elif option[0] == "q":
        os.system("cls")
        break
