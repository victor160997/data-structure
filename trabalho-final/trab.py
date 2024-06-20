import struct
import os

def readAluno(file):
    data = file.read(struct.calcsize('i18s'))
    if not data:
        return None, None
    mat, nome = struct.unpack('i18s', data)
    nome = nome.decode('latin-1').strip()
    return mat, nome
# ------------------------------------------------

def contarRegistros(filename):
    with open(filename, 'rb') as f:
        f.seek(0, os.SEEK_END)
        filesize = f.tell()
        return filesize // struct.calcsize('i18s')
# ------------------------------------------------


def gerarArquivosEntrada(filename="alunos.dat"):
    num_registros = contarRegistros(filename)
    metade = num_registros // 2
    
    with open(filename, 'rb') as bf, \
         open('f1.dat', 'wb') as f1, \
         open('f2.dat', 'wb') as f2:
        
        for i in range(num_registros):
            mat, nome = readAluno(bf)
            if i < metade:
                f1.write(struct.pack('i', mat))
                f1.write(bytes(nome, "latin-1"))
            else:
                f2.write(struct.pack('i', mat))
                f2.write(bytes(nome, "latin-1"))

        return f1, f2
# ------------------------------------------------


def writeAluno(file, mat, nome):
    file.write(struct.pack('i', mat))
    file.write(bytes(nome, 'latin-1'))
# ------------------------------------------------


def quicksort(alunos):
    if len(alunos) <= 1:
        return alunos
    else:
        pivot = alunos[len(alunos) // 2]
        left = [x for x in alunos if x[0] < pivot[0]]
        middle = [x for x in alunos if x[0] == pivot[0]]
        right = [x for x in alunos if x[0] > pivot[0]]
        return quicksort(left) + middle + quicksort(right)
# ------------------------------------------------


def ordenarArquivo(arquivoEntrada, arquivoSaida):
    alunos = []

    with open(arquivoEntrada, 'rb') as f:
        while True:
            mat, nome = readAluno(f)
            if mat is None:
                break
            alunos.append((mat, nome))

    alunos_ordenados = quicksort(alunos)

    with open(arquivoSaida, 'wb') as f:
        for mat, nome in alunos_ordenados:
            writeAluno(f, mat, nome)
    
    return arquivoSaida
# ------------------------------------------------


def gerarrquivoOrdenado():
    s1 = open('s1.dat', 'wb')
    s2 = open('s2.dat', 'wb')
    return s1, s2
# ------------------------------------------------


def gerarArquivoSaida():
    s = open('s.dat', 'wb')
    return s
# ------------------------------------------------


def externalMergeSort(file1, file2, s):
    with open(file1, 'rb') as f1, \
         open(file2, 'rb') as f2, \
         open(s, 'wb') as s:
        mat1, nome1 = readAluno(f1)
        mat2, nome2 = readAluno(f2)
        while mat1 is not None and mat2 is not None:
            if mat1 < mat2:
                writeAluno(s, mat1, nome1)
                mat1, nome1 = readAluno(f1)
            else:
                writeAluno(s, mat2, nome2)
                mat2, nome2 = readAluno(f2)
        
        while mat1 is not None:
            writeAluno(s, mat1, nome1)
            mat1, nome1 = readAluno(f1)
        
        while mat2 is not None:
            writeAluno(s, mat2, nome2)
            mat2, nome2 = readAluno(f2)

    return s
# ------------------------------------------------

    

def main():
    gerarArquivosEntrada()
    gerarrquivoOrdenado()

    ordenarArquivo("f1.dat", "s1.dat")
    ordenarArquivo("f2.dat", "s2.dat")

    gerarArquivoSaida()

    externalMergeSort("s1.dat", "s2.dat", "s.dat")

main()

    
