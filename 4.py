def ver_segundo_menor(vetor):
    n = len(vetor)
    menor_numero = vetor[0]
    segundo_menor = vetor[1]
    for i in range(1, n):
     if vetor[i] < menor_numero:
        menor_numero = vetor[i]
    for m in range(2, n):
       if vetor[m] > menor_numero and vetor[m]< vetor[i]:
        segundo_menor = vetor[m]
        print(segundo_menor)
       
lista = [7, 4, 1, 3, 9]
ver_segundo_menor(lista)