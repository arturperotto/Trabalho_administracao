from rich import print

def menu(nome_empresa , cor ="bold red"):
    print("=" * 40)
    print("{:^50}".format(f"[{cor}]{nome_empresa}[/]"))
    print("=" * 40)

def opcoes(*opcoes):
    lista_opcoes = []
    for o in opcoes:
        lista_opcoes.append(o)
    
    for n , l in enumerate(lista_opcoes):
        print(f"[{n + 1}] - {l}")

def name_show(nome , color="white"):
    print(f"[{color}]olá senhor {nome}[/]")
    print("=" * 30)

