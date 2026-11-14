import validador_cpf
import funcoes_cargos.funcoes_nivel1 as f1

#from tkinter import filedialog
#import shutil
#
#arquivo  = filedialog.askopenfilename()
#destino = "C:/Users/User/Desktop/trabalho administracao/cartas_desligamento"
#
#arquivo_copiado = shutil.copy(arquivo , destino)

nome = str(input("Nome do funcionário: "))

while True:
    cpf = str(input("CPF do funcionário: "))
    if validador_cpf.validador_cpf(cpf):
        cargo = str(input("Qual o cargo do funcionário: "))
        nivel_cargo = str(input("Qual o nivel do cargo do funcionário: "))
        f1.add_workers(nome , cpf , cargo , nivel_cargo)