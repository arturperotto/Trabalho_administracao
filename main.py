import interface as i
import validador_cpf
import validador_de_cargo  as vc
import funcoes_cargos.funcoes_nivel1 as f1
from sys import exit
from rich import print
from time import sleep

nivel_cargo = 0

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

elif opcao == 2:
    exit

print("  ")

if nivel_cargo == 1:
    i.name_show(nome , "bold white")

    while True:
        print("O que gostaria de fazer: ")
        i.opcoes("Adicionar funcionários" , "Demitir" , "Olhar pessoas cadastradas" , "mostrar atestados" , "mostrar ponto" , "sair")
        opcao = int(input("O que deseja fazer hoje: "))
        
        if opcao == 1:
            nome = str(input("Nome do funcionário: "))
            
            while True:
                cpf = str(input("CPF do funcionário: "))
                if validador_cpf.validar_cpf(cpf):
                    cargo = str(input("Qual o cargo do funcionário: "))
                    nivel_cargo = str(input("Qual o nivel do cargo do funcionário[1-3]: "))
                    f1.add_workers(nome , cpf , cargo , nivel_cargo)
                    break

                else:
                    print("[bold red]informação inválida[/]")
        
        elif opcao == 2:
                nome = str(input("Nome do funcionário: "))
                while True:
                    cpf = str(input("CPF do funcionário: "))
                    if validador_cpf(cpf):
                        f1.delete_workers(nome , cpf)  

                    else:
                        print("[bold red]infromação inválda[/]")
                        sleep(1)

        elif opcao == 3:
            while True:
                f1.see_persons()
                opcao = str(input("deseja sair[S/N]: ")).upper()

                if opcao == "S":
                    break

                elif opcao == "N":
                    pass

        elif opcao == 4:
            cpf = str(input("digite o cpf do funcionário: "))
            if validador_cpf.validar_cpf(cpf):
                f1.show_notes(cpf)
                print(" ")

        elif opcao == 5:
            cpf = str(input("Digite o cpf do funcionário: "))
            if validador_cpf.validar_cpf(cpf):
                f1.show_points(cpf)

        elif opcao == 6:
            break

elif nivel_cargo == 2:
    pass

elif nivel_cargo == 3:
    pass