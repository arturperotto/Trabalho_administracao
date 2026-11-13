from rich import print

def menu(nome_empresa):
    print("=" * 40)
    print("{:^50}".format(f"[bold red]{nome_empresa}[/]"))
    print("=" * 40)

def opcoes(*opcoes):
    lista_opcoes = []
    for o in opcoes:
        lista_opcoes.append(o)
    
    for n , l in enumerate(lista_opcoes):
        print(f"[{n + 1}] - {l}")