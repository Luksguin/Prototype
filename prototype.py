import numpy as np

name_file = input('Nome do arquivo: ')

def prototype(name):
    mat = np.loadtxt('grafos_datasets/' + name + '.txt')
    print(mat)

    i, j = mat.shape

    print(i)
    print(j)

    with open('outputs/' + name + '_output.txt', 'w') as file:
         file.write(name + ' ' + str(i) + ' ' + str(j))


prototype(name_file)
