codigos = {101, 102, 103, 104, 105}

codigos.remove(103)
print(codigos)

codigos.discard(999)    
#Em casos que não sabemos se o elemento existe, podemos usar o discard pois ele não retorna erro,
#com isso, evita falhas inesperadas e não interrompe a execução.