from time import strftime
from rich.table import Table
from rich import print

def add_workers(name , cpf , cargo ,nivel_cargo):
    a = open(f"Trabalhadores/{nivel_cargo}.txt" , "a")
    a.write(f"{name},{cpf},{cargo}\n")

def delete_workers(nome , cpf):
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

    for n in range(1,4):
        a = open(f"Trabalhadores/nivel{n}.txt" , encoding="utf-8")
        
        for l in a:
            l = l.replace("\n" , "")
            lista = l.strip().split(",")
            nomes[n].append(lista[0])
            cpfs[n].append(lista[1])      

        a.close()

    for nivel , cpfs in cpfs.items():
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

    for n in range(1,4):
        a = open(f"Trabalhadores/nivel{n}.txt" , encoding="utf-8")
        
        for l in a:
            l = l.replace("\n" , "")
            lista = l.strip().split(",")
            nomes.append(lista[0])
            cpfs.append(lista[1])  
            cargos.append(lista[2])

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

