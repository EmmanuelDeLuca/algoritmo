############################## HEAP DE MINIMO #####################################
def troca_elemento(vetor, i, aux):
    vetor[i], vetor[aux] = vetor[aux], vetor[i]

def left(i):
    return (2 * i) + 1

def right(i):
    return (2 * i) + 2

def max_heapify(veeetor, i):
    tamanho_do_heap = len(veeetor) - 1
    l = left(i)
    r = right(i)
    if l <= tamanho_do_heap and veeetor[l] < veeetor[i]:
        maior = l
    else:
        maior = i
    if r <= tamanho_do_heap and veeetor[r] < veeetor[maior]:
        maior = r
    if maior != i:
        troca_elemento(veeetor, i, maior)
        max_heapify(veeetor, maior)

def build_max_heap(veeetor):
    tamanho_do_heap = len(veeetor)
    for i in range(tamanho_do_heap,tamanho_do_heap//2, -1):
        max_heapify(veeetor, i)

vetor2 = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
max_heapify(vetor2, 0)
print(vetor2)
