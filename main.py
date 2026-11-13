import interface as i
import validador_cpf
from sys import exit
from time import sleep
from rich import print

while True:
    try:
        i.menu("Eletronor")
        i.opcoes("Entrar" , "Sair")
        opcao = int(input("oq deseja[opcão em número]: "))

        if opcao == 1 or opcao == 2:
            break
        else:
            pass

    except:
        print("[red]Resposta inválida![/]")
        sleep(1)

if opcao == 1:
    while True:
        cpf = str(input("Digite seu cpf: "))
        if validador_cpf.validar_cpf(cpf):
            nome = str(input("Digite seu nome: "))
            

        else:
            pass

if opcao == 2:
    exit