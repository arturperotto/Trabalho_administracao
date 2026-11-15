import validador_cpf
import funcoes_cargos.funcoes_nivel1 as f1

#from tkinter import filedialog
#import shutil
#
#arquivo  = filedialog.askopenfilename()
#destino = "C:/Users/User/Desktop/trabalho administracao/cartas_desligamento"
#
#arquivo_copiado = shutil.copy(arquivo , destino)
import os
import cv2

def show_notes(cpf):

    pasta = f"pontos,folhas/{cpf}/atestados"

    arquivos = os.listdir(pasta)

    for i, arquivo in enumerate(arquivos):
        if "txt" in arquivo:
            pass

        else:
            print(f"{i + 1} - {arquivo}")

    escolha = int(input("Qual atestado deseja abrir? "))

    caminho = os.path.join(pasta, arquivos[escolha - 1])

    imagem = cv2.imread(caminho)

    if imagem is None:
        print("Não foi possível abrir a imagem.")
        return

    cv2.imshow("Atestado", imagem)
    cv2.waitKey(0)
    cv2.destroyAllWindows()