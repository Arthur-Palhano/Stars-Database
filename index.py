from prettytable import PrettyTable
import math, os, json

def createTable():
    table = PrettyTable()
    table.field_names = ["Estrela", "Tipo", "Temp. (K)", f"Lum. (○)", f"Massa (M○)", "Comp. de Onda (μm)", f"Raio (R○)", "Mag. Aparente", "Mag. Absoluta", "Dist (LY)", "K"]
    table.sortby = "Estrela"
    return table

def loginStar():
    star = []
    star.append(str(input("Nome da Estrela: ")))#0
    star.append(str(input("Tipo: ")))#1
    star.append(float(input("Temperatura em Kelvin: ")))#2
    star.append(float(input("Luminosidade em ○: ")))#3
    star.append(float(input("Massa em ○: ")))#4
    star.append(float(input("Comprimento de Onda em μm: ")))#5
    star.append(float(input("Raio em ○: ")))#6
    star.append(float(input("Magnitude Aparente: ")))#7
    star.append(float(input("Magnitude Absoluta: ")))#8
    star.append(float(input("Distância em LY: ")))#9

    os.system("cls")
    
    L = star[3] * (3.9*(10**26))
    r = 3 * 10**17
    F = L/(4 * math.pi * (r**2))
    k = star[8] + 2.5 * math.log10(F)

    star.append(k)

    return star

def readJson():
    with open("stars.json", "r") as file:
        data = json.load(file)
    return data

def writeJson(stars):
    with open("stars.json", "w") as file:
        json.dump(stars, file, indent=5)

def resetJson():
    file = open("stars.json", "w")
    file.write("[]")
    file.close()

while True:
    table = createTable()
    stars = readJson()
    for star in stars:
        table.add_row(star)

    print()
    print(table)
    print()
    print("[A] - Add Estrela || [R] - Remover Estrela || [Q] - Sair || [RESET] - Resetar Estrelas")
    option = str(input("O que deseja fazer: "))
    option = option.lower()
    option = option.split(" ")

    if option[0] == "a":
        newStar = loginStar()
        stars.append(newStar)
        writeJson(stars)
        table.add_row(newStar)

    if option[0] == "r":
        name = str(input("Nome da Estrela: ")).lower()
        for star in stars:
            if star[0].lower() == name:
                del(stars[stars.index(star)])
                writeJson(stars)

    elif option[0] == "reset":
        if "confirmar" == str(input("Escreva (confirmar)")).lower():
            resetJson()

    elif option[0] == "c":
        os.system("cls")

    elif option[0] == "q":
        break
