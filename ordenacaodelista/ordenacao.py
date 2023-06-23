############################### ALGORITMO DE ORDENAÇÃO #####################################
# O ALGORITMO BUBBLE_SORT
'''def troca_elementos(vetor, index, indext):
    vetor[index], vetor[indext] = vetor[indext], vetor[index]

def bubble_sort(vetor, tamanho):
    for c in range(tamanho-1, 0, -1):
        for j in range(0, c):
            if vetor[j] > vetor[j+1]:
                troca_elementos(vetor, j, j+1)


numvetor = [6, 3, 9, 100, 24, 1, 0, 36, 44]
bubble_sort(numvetor, len(numvetor))

print(numvetor)'''


###################################### SELECTION SORT ########################################
# SELECTION_SORT
'''def troca_elementos(vetor, index, indext):
    vetor[index], vetor[indext] = vetor[indext], vetor[index]

def selection_sort(vetor, tamanho):
    for c in range(0, tamanho):
        min = c
        for j in range(c+1, tamanho):
            if vetor[min] > vetor[j]:
                min = j
        troca_elementos(vetor,c, min)


numvetor = [6, 3, 9, 100, 24, 1, 0, 36, 44]
selection_sort(numvetor, len(numvetor))

print(numvetor)'''


############################# INSERTION SORT #####################################
# INSERTION SORTE 
'''def insertion_sort(vetor, tamanho):
    for c in range(1, tamanho):
        aux = vetor[c]
        j = c - 1
        while j >= 0 and vetor[j] > aux:
            vetor[j+1] = vetor[j]
            j = j - 1
        vetor[j+1] = aux

numvetor = [6, 3, 9, 100, 24, 1, 0, 36, 44]
insertion_sort(numvetor, len(numvetor))

print(numvetor)'''

################################ SHELL SORT ##############################################
# SHELL SORT 
'''def troca_elementos(vetor, index, indext):
    vetor[index], vetor[indext] = vetor[indext], vetor[index] 

def shell_sort(vetor, tamanho):
    h = 1
    while h < tamanho//3:
        h = 3*h + 1
    while h >= 1:
        for i in range(h, tamanho):
            j = i
            while j >= h and vetor[j] < vetor[j - h]:
                troca_elementos(vetor, j, j-h)
                j = j - h
        h = h//3

numvetor = [6, 3, 9, 100, 24, 1, 0, 36, 44]
shell_sort(numvetor, len(numvetor))

print(numvetor)'''
################################ ALGORITMO DE ORDENAÇÃO AVANÇADO #####################
################################# MERGESORT ####################################
'''def merge(v, esquerda, meio, direita):
    i = esquerda
    j = meio + 1
    aux = list(v)

    for k in range(esquerda, direita+1):
        aux[k] = v[k]
    for k in range(esquerda, direita+1):
        if i > meio:
            v[k]= aux[j]
            j = j + 1
        elif j > direita:
            v[k] = aux[i]
            i = i + 1
        elif aux[i] > aux[j]:
            v[k] = aux[j]
            j = j + 1
        else:
            v[k] = aux[i]
            i = i + 1

def TD_mergesort(v, esquerda, direita): ###### TOP-DOWN ###
    if esquerda >= direita:
        return
    meio = (esquerda+direita)//2
    TD_mergesort(v, esquerda, meio)
    TD_mergesort(v, meio+1, direita)
    merge(v, esquerda, meio, direita)

def mergue_sort(v, N):
    aux = list(v)
    TD_mergesort(v, 0, N-1)
    del aux

numvetor = [6, 3, 9, 100, 24, 1, 0, 36, 44]

mergue_sort(numvetor, len(numvetor))
print(numvetor)'''
############ VERSAO ITERATIVA DO MERGESORT #########################

'''def iterativa_merge_sort(vetor, N):
    aux = list(vetor)
    k = 1
    while k < N:
        for esq in range(0, N-k, 2*k):
            merge(vetor, esq, esq+k-1, min(esq + (2*k) - 1, N-1))
        k = k * 2
    
    del aux

aux = []
vetor = [5, 7, 10, 3, 4, 60, 23, 429, 100, 10, 467]
iterativa_merge_sort(vetor, len(vetor))

print(vetor)'''



