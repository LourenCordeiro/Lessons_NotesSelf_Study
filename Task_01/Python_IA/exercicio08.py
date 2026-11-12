numeros =set([10, 20, 30, 40, 50])

numeros.remove(30)
print(numeros)
#numeros.remove(100)    Quando usa o comando remove e não existe o elemento retorná um erro(Keyerror)
#Já o comando discard não retorna erro, ele apenas ignora o comando, quando o elemento não existe.
numeros.discard(100)
print(numeros)