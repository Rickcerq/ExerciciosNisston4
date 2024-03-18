pares = 0
impares = 0

vetor = [3, 1, 9, 4, 6]
n = len(vetor)
vetor.sort(reverse=True)
print (vetor)

for i in range(n):
    
 if vetor[i] % 2 == 0:
    pares += 1
    print ('Quantidade de numeros pares:', pares)

 else:
    impares += 1
    print ('Quantidade de numeros impares:', impares)