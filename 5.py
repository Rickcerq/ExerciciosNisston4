numero = int(input('Digite o numero para pesquisar se ele foi repetido: '))

def remover_repetido(vetor):
    
     if vetor.count(numero) > 1:
      while numero in vetor:
         vetor.remove(numero)
         print('A lista após a remoção:', vetor)
     else:
        print('O valor não foi repetido, a lista permanece a mesma:')

lista = [4, 2, 9, 2, 1, 8, 9]
remover_repetido(lista)
