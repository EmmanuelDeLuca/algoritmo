#################################### HASHING ############################################

class Hashing:
    def __init__(self, cedula, index):
        self.proximo = None
        self.cedula = cedula
        self.index = index

class Hashing_Aberto:
    def __init__(self):
        self.cabeca = None
        self.macador_index = 0

    def insercao_hashing(self, x):
        novo_elemento = Hashing(x, self.macador_index)

        if self.cabeca == None:
          self.cabeca = novo_elemento
          self.macador_index += 1
          return
        
        ponteiro = self.cabeca
        while ponteiro.proximo:
            ponteiro = ponteiro.proximo
      
        ponteiro.proximo = novo_elemento
        self.macador_index += 1

    def buscar_hashig(self, cafe):
      ponteiro = self.cabeca
      while ponteiro.proximo:
        if ponteiro.cedula >= cafe:
          pass
        else:
          aux = cafe - ponteiro.cedula
          index  = self.busquinha_hashing(aux)
          if index != None:
            ponteiro.proximo = None
            return ponteiro.index , index
        ponteiro = ponteiro.proximo

    def busquinha_hashing(self,x):
      ponteiro = self.cabeca

      for c in range(self.macador_index):
        if ponteiro.cedula == x:
          return ponteiro.index
        ponteiro = ponteiro.proximo

        


qtd_notas = int(input())
aux = Hashing_Aberto()
for c in range(qtd_notas):
    aux.insercao_hashing(int(input()))

index1, index2 = aux.buscar_hashig(int(input()))
if index1 != None and index2 != None:
  print('[{}, {}]'.format(index1, index2))
else:
  print('Sem cafe da manha dessa vez :/')