import struct

def list_alunos_from_dat(filename="s.dat"):
    try:
        with open(filename, "rb") as f:
            while True:
                data = f.read(struct.calcsize('i18s'))
                if not data:
                    break
                mat, nome = struct.unpack('i18s', data)
                nome = nome.decode('utf-8').strip()
                print(f"Matricula: {mat}, Nome: {nome}")
    except FileNotFoundError:
        print(f"O arquivo {filename} não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

list_alunos_from_dat()