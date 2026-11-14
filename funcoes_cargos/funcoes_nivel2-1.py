from datetime import datetime
from tkinter import filedialog
import os
import cv2
import shutil

def clock_in(cpf):
    hora = datetime.now().strftime("%H:%M")
    dia = datetime.now().strftime("%d/%m/%Y")
    a = open(f"pontos,folhas/{cpf}/pontos/datas.txt" , "a")

    a.write(f"chegada, dia {dia},hora {hora}\n")

def clock_out(cpf):
    hora = datetime.now().strftime("%H:%M")
    dia = datetime.now().strftime("%d/%m/%Y")
    a = open(f"pontos,folhas/{cpf}/pontos/datas.txt" , "a")

    a.write(f"saida, dia {dia},hora {hora}\n")

def put_note(cpf):
    dia = datetime.now().strftime("%d/%m/%Y")
    a = open(f"pontos,folhas/{cpf}/atestados/datas.txt" , "a")
    a.write(f"*atestado dia {dia}\n")

    arquivo  = filedialog.askopenfilename()
    destino = f"pontos,folhas/{cpf}/folhas_de_pagamento"
    arquivo_copiado = shutil.copy(arquivo , destino)

def post_payroll(cpf):
    pasta = f"pontos,folhas/{cpf}/folhas_de_pagamento"

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