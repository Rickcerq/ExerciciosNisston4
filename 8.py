def mostrar_mediana(vetor):
    vetor.sort()
    n = len(vetor)
    mediana = vetor[n//2]
    print ('Lista ordenada:', vetor)
    print ('Mediana da lista ordenada:', mediana)

lista = [4, 2, 9, 1, 5]
mostrar_mediana(lista)