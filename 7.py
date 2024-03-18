def ver_terceiro_maior_numero(vetor):
  n = len(vetor)
  maior_numero = vetor[0]
  segundo_maior = vetor[0]
  terceiro_maior = vetor[0]

  for i in range(1, n):
    if vetor[i] > maior_numero:
      maior_numero = vetor[i]
  
  for m in range(1, n):
    if vetor[m] > segundo_maior and vetor[m] < maior_numero:
      segundo_maior = vetor[m]

  for j in range(1, n):
    if vetor[j] > terceiro_maior and vetor[j] < segundo_maior:
      terceiro_maior = vetor[j]
      print ('O terceiro maior numero é:', terceiro_maior)

lista = [3, 9, 2, 6, 7]
ver_terceiro_maior_numero(lista)