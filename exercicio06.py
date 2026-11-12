numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

soma = numero1 + numero2
print(f"A soma dos números inteiros é {soma}")

divisao_inteira = numero1 // numero2
print(f"A divisão inteira dos números inteiros é {divisao_inteira}")

resto_da_divisao = numero1 % numero2
print(f"O resto da divisão dos números inteiros é {resto_da_divisao}")

maior_que_10 = numero1 > 10 and numero2 > 10
numeros_diferentes = numero1 != numero2

print(f"Os números {numero1} e {numero2} são maiores que 10? {maior_que_10}")
print(f"Os números {numero1} e {numero2} são diferentes? {numeros_diferentes}")
