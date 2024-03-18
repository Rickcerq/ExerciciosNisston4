def selection_sort_crescente(vetor):
 n = len(vetor)

 for i in range(n):
  id_minimo = i
  for j in range(i + 1, n):
    if vetor[id_minimo] > vetor[j]:
     id_minimo = j
  temp = vetor[i]
  vetor[i] = vetor[id_minimo]
  vetor[id_minimo] = temp
 return vetor

def selection_sort_decrescente(vetor):
 n = len(vetor)

 for i in range(n):
  id_minimo = i
  for j in range(i + 1, n):
    if vetor[id_minimo] < vetor[j]:
     id_minimo = j
  temp = vetor[i]
  vetor[i] = vetor[id_minimo]
  vetor[id_minimo] = temp
 return vetor

vetor = [2, 9, 1, 3, 5]
x = int(input('Digite: 1 - se quiser que sua ordenação seja crescente, ou 2 - se quiser que sua ordenação seja decrescente: '))

if x == 1:
 selection_sort_crescente(vetor)
 print ('Lista ordenada de forma crescente:', vetor)

else:
 selection_sort_decrescente(vetor)
 print ('Lista ordenadada de forma decrescente:', vetor)