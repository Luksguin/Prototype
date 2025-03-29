# Importação de bibliotecas e inputs
import numpy as np

name_file = input('Nome do arquivo: ')

def prototype(name):
# Leitura do dataset e associação a uma matriz, e também sua impressão
    mat = np.loadtxt('grafos_datasets/' + name + '.txt')
    print(mat)

# Acessando e imprimindo as dimensões da matriz
    i, j = mat.shape 

    print(i)
    print(j)

# Criação/abertura de um arquivo que armazenará a saída
    with open('outputs/' + name + '_output.txt', 'w') as file:
         file.write(name + ' ' + str(i) + ' ' + str(j))

# Chamadas das funções
prototype(name_file)
