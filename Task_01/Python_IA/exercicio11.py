nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

peso1 = 4
peso2 = 6

media_ponderada = (nota1 * peso1 + nota2 * peso2) / (peso1 + peso2)

aprovado = media_ponderada >= 7.0 and nota1 >= 5.0 and nota2 >= 5.0

print(f"A media ponderada é: {media_ponderada:.2f}")
print(f"Aprovado: {aprovado} ")






