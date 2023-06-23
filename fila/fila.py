##################### FILA #####################################
class Ligacao:
  def __init__(self,chave,tempo):
    self.tempo = tempo
    self.chave = chave
    self.proximo = None

class Fila:
  def __init__(self):
    self.tamanho = 0
    self.comeco = None
    self.fim = None
    self.exe = 0

  def enqueue(self, x,y):
    add = Ligacao(x,y)
    if self.tamanho == 0:
      self.fim = add
      

    elif self.comeco == None:
      self.comeco = add
      
    
    else:
      self.fim.proximo = add
      self.fim = add
      
    self.tamanho += 1
    print("O programa {} foi agendado com sucesso!".format(add.chave))
    
  # add 0 10
  # exe 8


  def dequeue(self,x):
    aux = self.tamanho
    add = self.comeco
    if self.tamanho == 0:
      print('Lista vazia')
    else:
      self.exe = x
      while aux != None:
        print('o tempo do programa {} foi {}'.format(add.chave, add.tempo))
        add = add.proximo

    '''self.exe = x
    add = self.cabeca
    aux = self.tamanho
    if self.tamanho > 0:
      print("O programa {} executou por {} segundos.".format(add.chave, add.tempo))
      while add != None:
        if self.exe > 0:
          if add.tempo ==  self.exe:
            print('O programa {} terminou.'.format(add.chave))
            aux -= 1
            self.exe = self.exe - add.tempo
            add = add.proximo
          elif add.tempo > self.exe:
            add.tempo = add.tempo - self.exe
            add = add.proximo
          elif add.tempo < self.exe:
            print('O programa {} terminou.'.format(add.chave))
            self.exe = self.exe - add.tempo
            aux = aux - 1
            add = add.proximo
        else:
          pass
      print('A linha possui {} programas.'.format(aux))
    else: 
      print('Fila esta vazia')'''

def main():
  n = int(input())
  while n <= 0:
    n = int(input())
  comando2 = Fila()
  for i in range(n):
    comando1 = input()
    comando1 = comando1.split()
    if len(comando1) == 3 and (comando1[0] == 'ADD'):
      chave = int(comando1[1])
      tempo = int(comando1[2])
      comando2.enqueue(chave,tempo)
        
    elif len(comando1) == 2 and (comando1[0] == 'EXE'):
      remocao = int(comando1[1])
      comando2.dequeue(remocao)
    elif len(comando1) == 0:
      print('Lista esta vazia')
    else:
      pass

if __name__ == '__main__':
    main()


'''def dequeue(self,x):
    self.exe = x
    add = self.cabeca
    aux = self.tamanho
    if self.tamanho > 0:
      print("O programa {} executou por {} segundos.".format(add.chave, add.tempo))
      for c in range(self.tamanho):
        self.exe -= add.tempo 
        if add.tempo == 0:
          print('O programa {} terminou.'.format(add.chave))
          aux -= 1
          add = add.proximo
        elif add.tempo > 0:
          add = add.proximo
        elif x > 0 and add.tempo == 0:
          print('O programa {} terminou.'.format(add.chave))
          aux -= 1
          add = add.proximo
      print('A linha possui {} programas.'.format(c))
    elif self.tamanho == 0:
      print('Fila esta vazia')
    else:
      pass'''