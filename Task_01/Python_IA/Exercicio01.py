preco = 150.00
desconto = 20

preco_com_desconto = preco * (1 - desconto / 100)
valor_do_desconto = preco - preco_com_desconto

print(f"O produto no valor de R${preco:.2f}".replace('.', ',') + f" com {desconto}% de desconto, ficará no valor de R${preco_com_desconto:.2f}!".replace('.', ','))