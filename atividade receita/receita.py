import glob
import os

def gravar_receita():
    nome = input("Nome da receita: ")
    ingredientes = []
    while True:
        ingrediente = input("Ingrediente (ou 'fim' para encerrar): ")
        if ingrediente == 'fim':
            break
        ingredientes.append(ingrediente)
    modo_preparo = input("Modo de preparo: ")
    
    with open(f"{nome.strip()}.txt", "a") as file:
        file.write(f"Nome da receita: {nome}\n")
        file.write("Ingredientes:\n")
        for ingrediente in ingredientes:
            file.write(f"- {ingrediente}\n")
        file.write(f"Modo de preparo: {modo_preparo}\n")
        file.write("\n")

def listar_receitas():
    for file_name in glob.glob("*.txt"):
        with open(file_name, "r") as file:
            print("\033[45m" + file.read() + "\033[0m")

def consultar_receita():
    nome = input("Digite o nome da receita: ")
    with open(f"{nome}.txt", "r") as file:
        receitas = file.read().split("\n\n")
        for receita in receitas:
            if nome in receita:
                print("\033[45m" + receita + "\033[0m")

def deletar_receita():
    nome = input("Digite o nome da receita a ser deletada:")
    file_path = f"{nome}.txt"
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"Receita '{file_path}' deletada com sucesso.")
    else:
        print(f"Receita '{file_path}' não existe.")

while True:
    print("1 – Criar Receita")
    print("2 – Consultar Receita")
    print("3 – Listar Receitas")
    print("4 – Deletar Receita")
    print("5 – Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == '1':
        gravar_receita()
    elif opcao == '2':
        consultar_receita()
    elif opcao == '3':
        listar_receitas()
    elif opcao == '4':
        deletar_receita()
    elif opcao == '5':
        break
    else:
        print("Opção inválida. Tente novamente.")