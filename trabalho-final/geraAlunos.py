import random
import string
import struct

def generate_random_name(length=18):
    letters = string.ascii_uppercase + string.ascii_lowercase
    name = ''.join(random.choice(letters) for i in range(length))
    return name.ljust(length)[:length]

def generate_alunos_dat(filename="alunos.dat", num_alunos=10):
    with open(filename, "wb") as f:
        for _ in range(num_alunos):
            mat = random.randint(10, 99)
            nome = generate_random_name()
            # 'i' para inteiro e '18s' para string de 18 caracteres
            f.write(struct.pack('i18s', mat, nome.encode('utf-8')))

# Executa a função para gerar o arquivo alunos.dat
generate_alunos_dat()