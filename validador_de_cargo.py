def validador_nivel3(nome, cpf):
    a = open("trabalhadores/nivel3.txt", encoding="UTF-8")
    nomes = []
    cpfs = []
    cargos = []

    for n ,i in enumerate(a):
        lista = i.strip().split(",")
        nomes.append(lista[0])
        cpfs.append(lista[1])
        cargos.append(lista[2])

        print(nomes[n] , cpfs[n])

        if nome == nomes[n]:
            if cpf == cpfs[n]:
                return True, cargos[n]
        else:
            pass
        
    return False

def validadaor_nivel2(nome, cpf):
    a = open("trabalhadores/nivel2.txt", encoding="UTF-8")
    nomes = []
    cpfs = []
    cargos = []

    for n ,i in enumerate(a):
        lista = i.strip().split(",")
        nomes.append(lista[0])
        cpfs.append(lista[1])
        cargos.append(lista[2])

        if nome == nomes[n]:
            if cpf == cpfs[n]:
                return True, cargos[n]
        else:
            pass
        
    return False

def validadaor_nivel1(nome, cpf):
    a = open("trabalhadores/nivel1.txt", encoding="UTF-8")
    nomes = []
    cpfs = []
    cargos = []

    for n ,i in enumerate(a):
        lista = i.strip().split(",")
        nomes.append(lista[0])
        cpfs.append(lista[1])
        cargos.append(lista[2])

        if nome == nomes[n]:
            if cpf == cpfs[n]:
                return True, cargos[n]
        else:
            pass
        
    return False