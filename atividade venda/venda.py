import struct
import os

record_format = 'i19s7s'
record_size = struct.calcsize(record_format)

def criar_arquivo():
    nome_do_arquivo = input("Digite o nome do arquivo: ")
    with open(f'{nome_do_arquivo}.dat', 'wb') as file:
        file.close()

def listar_registros():
    nome_do_arquivo = input("Digite o nome do arquivo que deseja listar os registros: ")
    with open(f'{nome_do_arquivo}.dat', 'rb') as file:
        while True:
            record = file.read(record_size)
            if not record:
                break
            codigo, valor, mes_ano = struct.unpack(record_format, record)
            print(f'Código Vendedor: {codigo}, Valor: {valor.decode()}, Mês/Ano: {mes_ano.decode()}')

def incluir_vendedor():
    codigo = int(input("Digite o código do vendedor: "))
    valor = float(input("Digite o valor total da venda: "))
    mes_ano = input("Digite o mês e ano da venda (MM/AAAA): ")
    nome_do_arquivo = input("Digite o nome do arquivo: ")
    with open(f'{nome_do_arquivo}.dat', 'ab') as file:
        file.seek(0, os.SEEK_END)
        file.write(struct.pack(record_format, codigo, str(valor).encode()[:19], str(mes_ano).encode()[:7]))

while True:
    print(record_size)
    print("1 – Criar arquivo de dados")
    print("2 – Incluir um determinado vendedor no arquivo")
    print("3 – Excluir um determinado vendedor no arquivo")
    print("4 – Alterar o valor total da venda de um determinado vendedor de um determinado mês")
    print("5 – Imprimir os registros na saída padrão")
    print("6 – Consultar o vendedor com maior valor da venda")
    print("7 – Finalizar o programa.")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == '1':
        criar_arquivo()
    elif opcao == '2':
        incluir_vendedor()
    # elif opcao == '3':
    #     excluir_vendedor()
    # elif opcao == '4':
    #     alterar_valor_venda()
    elif opcao == '5':
        listar_registros()
    # elif opcao == '6':
    #     pegar_vendedor_maior_venda()
    # elif opcao == '7':
        break
    else:
        print("Opção inválida. Tente novamente.")