import struct
import os

record_format = 'i19s7s'
record_size = struct.calcsize(record_format)
type_file_name = 'Digite o nome do arquivo: '

def criar_arquivo():
    nome_do_arquivo = input(type_file_name)
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
            print('\033[41m' + f'Código Vendedor: {codigo}, Valor: {valor.decode()}, Mês/Ano: {mes_ano.decode()}' + '\033[0m')

def incluir_vendedor():
    nome_do_arquivo = input(type_file_name)
    codigo = int(input("Digite o código do vendedor: "))
    valor = float(input("Digite o valor total da venda: "))
    mes_ano = input("Digite o mês e ano da venda (MM/AAAA): ")
    with open(f'{nome_do_arquivo}.dat', 'ab') as file:
        file.seek(0, os.SEEK_END)
        file.write(struct.pack(record_format, codigo, str(valor).encode()[:19], str(mes_ano).encode()[:7]))

def deleta_vendedor_pelo_codigo():
    nome_do_arquivo = input(type_file_name)
    codigo = int(input("Digite o código do vendedor que deseja excluir: "))
    with open(f'{nome_do_arquivo}.dat', 'rb') as file:
        with open(f'{nome_do_arquivo}_temp.dat', 'wb') as temp_file:
            while True:
                record = file.read(record_size)
                if not record:
                    break
                record_codigo, valor, mes_ano = struct.unpack(record_format, record)
                if record_codigo != codigo:
                    temp_file.write(struct.pack(record_format, record_codigo, valor, mes_ano))
    os.remove(f'{nome_do_arquivo}.dat')
    os.rename(f'{nome_do_arquivo}_temp.dat', f'{nome_do_arquivo}.dat')

def altera_valor_venda():
    nome_do_arquivo = input(type_file_name)
    codigo = int(input("Digite o código do vendedor que deseja alterar: "))
    mes_ano = input("Digite o mês e ano da venda (MM/AAAA): ")
    novo_valor = float(input("Digite o novo valor da venda: "))
    with open(f'{nome_do_arquivo}.dat', 'rb') as file:
        with open(f'{nome_do_arquivo}_temp.dat', 'wb') as temp_file:
            while True:
                record = file.read(record_size)
                if not record:
                    break
                record_codigo, valor, record_mes_ano = struct.unpack(record_format, record)
                if record_codigo == codigo and record_mes_ano.decode() == mes_ano:
                    temp_file.write(struct.pack(record_format, record_codigo, str(novo_valor).encode()[:19], record_mes_ano))
                else:
                    temp_file.write(struct.pack(record_format, record_codigo, valor, record_mes_ano))
    os.remove(f'{nome_do_arquivo}.dat')
    os.rename(f'{nome_do_arquivo}_temp.dat', f'{nome_do_arquivo}.dat')

def pega_vendedor_com_maior_venda():
    nome_do_arquivo = input("Digite o nome do arquivo que deseja pegar a maior venda: ")
    codigo_mv, valor_mv, mes_ano_mv = 0, 0, ''
    with open(f'{nome_do_arquivo}.dat', 'rb') as file:
        while True:
            record = file.read(record_size)
            if not record:
                break
            codigo, valor, mes_ano = struct.unpack(record_format, record)
            string_data = valor.decode('utf-8').strip('\x00')
            float_value = float(string_data)
            if float_value > valor_mv:
                codigo_mv, valor_mv, mes_ano_mv = codigo, float_value, mes_ano
    print('\033[42m' + 'O vendedor com a maior venda é:' + '\033[0m')
    print('\033[44m' + f'Código Vendedor: {codigo_mv}, Valor: {valor_mv}, Mês/Ano: {mes_ano_mv.decode()}' + '\033[0m')

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
    elif opcao == '3':
        deleta_vendedor_pelo_codigo()
    elif opcao == '4':
        altera_valor_venda()
    elif opcao == '5':
        listar_registros()
    elif opcao == '6':
        pega_vendedor_com_maior_venda()
    elif opcao == '7':
        break
    else:
        print("Opção inválida. Tente novamente.")