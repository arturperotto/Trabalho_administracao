from time import strftime
import os
from tkinter import filedialog
import shutil
from rich.table import Table
from rich import print
import cv2


def add_workers(name, cpf, cargo, nivel_cargo):
    a = open(f"Trabalhadores/nivel{nivel_cargo}.txt", "a")
    a.write(f"{name},{cpf},{cargo},ativo\n")
    folhas_depagamento = f"pontos,folhas/{cpf}/folha_pagamento/datas.txt"
    pontos = f"pontos,folhas/{cpf}/atestados/datas.txt"
    atestados = f"pontos,folhas/{cpf}/atestados/datas.txt"

    os.mkdir(f"pontos,folhas/{cpf}")
    os.mkdir(f"pontos,folhas/{cpf}/atestados")
    os.mkdir(f"pontos,folhas/{cpf}/pontos")
    os.mkdir(f"pontos,folhas/{cpf}/folha_pagamento")

    open(folhas_depagamento, "w").close()
    

def delete_workers(nome, cpf):
    time = strftime("%d/%m/%Y")
    nomes = {
        1: [],
        2: [],
        3: []
    }
    cpfs = {
        1: [],
        2: [],
        3: []
    }

    for n in range(1, 4):
        a = open(f"Trabalhadores/nivel{n}.txt", encoding="utf-8")

        for l in a:
            l = l.replace("\n", "")
            lista = l.strip().split(",")
            nomes[n].append(lista[0])
            cpfs[n].append(lista[1])

        a.close()

    for nivel, cpfs in cpfs.items():
        for n in cpfs:
            if cpf == n:
                nivel = nivel
                break

    nomes = []
    cpfs = []
    cargo = []

    a = open(f"trabalhadores/nivel{nivel}.txt", "r+", encoding="utf-8")

    linhas = a.readlines()
    a.seek(0)

    for n, l in enumerate(linhas):
        l = l.replace("\n", "")
        lista = l.strip().split(",")

        nomes.append(lista[0])
        cpfs.append(lista[1])
        cargo.append(lista[2])

        if nome == nomes[n]:
            if cpf == cpfs[n]:
                linhas[n] = f"{nome},{cpf},{cargo[n]},inativo,{time}\n"

    a.seek(0)
    a.writelines(linhas)
    a.truncate()
    a.close()


def see_persons():
    nomes = []
    cpfs = []
    cargos = []

    for n in range(1, 4):
        a = open(f"Trabalhadores/nivel{n}.txt")

        for l in a:
            l = l.replace("\n", "")
            lista = l.strip().split(",")
            
            if len(lista) < 4:
                continue
            
            elif lista[3] == "ativo":
                nomes.append(lista[0])
                cpfs.append(lista[1])
                cargos.append(lista[2])

            else:
                continue

    tabela = Table(title="TRABALHADORES")

    tabela.add_column("Nome", style="blue")
    tabela.add_column("CPF", style="blue")
    tabela.add_column("Cargo", style="blue")

    for n, nome in enumerate(nomes):
        tabela.add_row(
            nome,
            cpfs[n],
            cargos[n]
        )
    print(tabela)


def show_points(cpf):
    pasta = f"pontos,folhas/{cpf}/pontos"

    arquivos = os.listdir(pasta)

    for i, arquivo in enumerate(arquivos):
        if "txt" in arquivo:
            pass

        else:
            print(f"{i + 1} - {arquivo}")

    escolha = int(input("Qual ponto deseja abrir: "))

    caminho = os.path.join(pasta, arquivos[escolha - 1])

    imagem = cv2.imread(caminho)

    if imagem is None:
        print("Não foi possível abrir a imagem.")
        return

    cv2.imshow("ponto", imagem)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def show_notes(cpf):
    pasta = f"pontos,folhas/{cpf}/atestados"

    arquivos = os.listdir(pasta)

    for i, arquivo in enumerate(arquivos):
        if "txt" in arquivo:
            pass

        else:
            print(f"{i + 1} - {arquivo}")

    escolha = int(input("Qual atestado deseja abrir: "))

    caminho = os.path.join(pasta, arquivos[escolha - 1])

    imagem = cv2.imread(caminho)

    if imagem is None:
        print("Não foi possível abrir a imagem.")
        return

    cv2.imshow("Atestado", imagem)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def post_payroll(cpf):
    arquivo  = filedialog.askopenfilename()
    destino = f"pontos,folhas/{cpf}/folhas_de_pagamento"
    
    arquivo_copiado = shutil.copy(arquivo , destino)

post_payroll("16899535009")