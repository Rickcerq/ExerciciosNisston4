lista = [5, 1, 8, 9, 2]

n = len(lista)
maior_numero = lista[0]
menor_numero = lista[0]

for i in range(1, n):
    if lista[i] > maior_numero:
        maior_numero = lista[i]

for i in range(1, n):
    if lista[i] < menor_numero:
        menor_numero = lista[i]

print ('Maior numéro da lista:', maior_numero)
print ('Menor numéro da lista:', menor_numero)