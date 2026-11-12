pedidos10 = {"nome": "Notebook","preco": 3500.00, "estoque": 12}

if "desconto" in pedidos10:
    print(f"Desconto: {pedidos10['desconto']}%")
else:
    print("Este produto não tem desconto cadastrado.")