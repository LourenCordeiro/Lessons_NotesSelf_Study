ids = [101, 102, 101, 103, 104, 102, 105]

ids_unicos = set(ids)
print(ids_unicos)

if 103 in ids_unicos:
    print ("True")
else:
    print("False")

ids_lista = list(ids_unicos)
print(ids_lista)
#print(ids)

