numeros_lista = [1, 2, 2, 3, 4, 4, 5, 5]

print(numeros_lista)
numeros_set = set(numeros_lista)
print(numeros_set)

(numeros_set[0])
#TypeError: 'set' object is not subscriptable. O set não é indexado por índices mas sim por valores,
#por esse motivo ocorre o TypeError, por falha no acesso ao índice.