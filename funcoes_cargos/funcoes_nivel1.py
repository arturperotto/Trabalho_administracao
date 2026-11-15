from time import strftime
import os
from time import sleep
from tkinter import filedialog
import shutil
from rich.table import Table
from rich import print
import cv2

def path_exist(cpf):
    pasta = f"pontos,folhas/{cpf}"

    if os.path.exists(pasta):
        return True

    else:
        return False

def add_workers(name, cpf, cargo, nivel_cargo):
    a = open(f"Trabalhadores/nivel{nivel_cargo}.txt", "a" , encoding="cp1252")
    a.write(f"{name},{cpf},{cargo},ativo\n")
    folhas_depagamento = f"pontos,folhas/{cpf}/folha_pagamento/datas.txt"
    pontos = f"pontos,folhas/{cpf}/atestados/datas.txt"
    atestados = f"pontos,folhas/{cpf}/atestados/datas.txt"

    os.mkdir(f"pontos,folhas/{cpf}")
    os.mkdir(f"pontos,folhas/{cpf}/atestados")
    os.mkdir(f"pontos,folhas/{cpf}/pontos")
    os.mkdir(f"pontos,folhas/{cpf}/folha_pagamento")

    open(folhas_depagamento, "w").close()
    open(pontos, "w").close()
    open(atestados, "w").close()

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
        a = open(f"Trabalhadores/nivel{n}.txt", encoding="cp1252")

        for l in a:
            l = l.replace("\n", "")
            lista = l.strip().split(",")
            nomes[n].append(lista[0])
            cpfs[n].append(lista[1])

        a.close()

    for nivel, CPFs in cpfs.items():
        for n in CPFs:
            if cpf == n:
                nivel_atual = nivel
                break

    nomes = []
    cpfs = []
    cargo = []

    a = open(f"trabalhadores/nivel{nivel_atual}.txt", "r+", encoding="cp1252")

    linhas = a.readlines()
    a.seek(0)

    for n, l in enumerate(linhas):
        l = l.replace("\n", "")
        lista = l.strip().split(",")

        nomes.append(lista[0])
        cpfs.append(lista[1])
        cargo.append(lista[2])

        print("Nome recebido:", repr(nome))
        print("Nome encontrado:", repr(nomes[n]))
        print("São iguais?", nome == nomes[n])
        if nome == nomes[n]:
            if cpf == cpfs[n]:
                linhas[n] = f"{nome},{cpf},{cargo[n]},inativo,{time}\n"

    shutil.rmtree(f"pontos,folhas/{cpf}")
    a.seek(0)
    a.writelines(linhas)
    a.truncate()
    a.close()

def see_persons():
    nomes = []
    cpfs = []
    cargos = []

    for n in range(1, 4):
        a = open(f"Trabalhadores/nivel{n}.txt" , encoding="cp1252")

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

    if os.path.exists(pasta):
        if os.listdir(pasta):
            arquivos = os.listdir(pasta)

            for i, arquivo in enumerate(arquivos):
                if "txt" in arquivo:
                    pass

                else:
                    print(f"{i} - {arquivo}")

            escolha = int(input("Qual ponto deseja abrir: "))

            caminho = os.path.join(pasta, arquivos[escolha])

            imagem = cv2.imread(caminho)

            if imagem is None:
                print("Não foi possível abrir a imagem.")
                return

            cv2.imshow("ponto", imagem)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        else:
            print("Arquivo vazio")
            sleep(1)
    else:
        print("Arquivo não existe")

def show_notes(cpf):
    pasta = f"pontos,folhas/{cpf}/atestados"

    arquivos = os.listdir(pasta)

    for i, arquivo in enumerate(arquivos):
        if "txt" in arquivo:
            pass

        else:
            print(f"{i} - {arquivo}")

    escolha = int(input("Qual atestado deseja abrir: "))

    caminho = os.path.join(pasta, arquivos[escolha])

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