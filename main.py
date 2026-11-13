import interface as i
import validador_cpf
import validador_de_cargo  as vc
from sys import exit
from time import sleep
from rich import print

while True:
    try:
        i.menu("Eletronor")
        i.opcoes("Entrar" , "Sair")
        opcao = int(input("oq deseja: "))

        if opcao == 1 or opcao == 2:
            break
        else:
            pass

    except:
        print("[red]Resposta inválida![/]")
        sleep(1)

if opcao == 1:
    while True:
        nome = str(input("Digite seu nome: "))
        cpf = str(input("Digite seu cpf[bote apenas os números]: "))
        
        if validador_cpf.validar_cpf(cpf):
            if vc.validadaor_nivel1(nome , cpf):
                nivel_cargo = 1
                cargo = vc.validadaor_nivel1(nome , cpf)
                break
            
            else:
                if vc.validadaor_nivel2(nome , cpf):
                    nivel_cargo = 2
                    cargo = vc.validadaor_nivel1(nome , cpf)
                    break

                else:
                    if vc.validador_nivel3(nome,cpf):
                        nivel_cargo = 3
                        cargo = vc.validador_nivel3(nome , cpf)
                        break

                    else:
                        print("[bold red]Usuário não cadastrado[/]")
                        break      
        else:
            print("[bold red]Informação inválida inválido[/]")
            sleep(1)
            pass

if opcao == 2:
    exit

