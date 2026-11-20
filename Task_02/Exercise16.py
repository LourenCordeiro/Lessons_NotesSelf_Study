import pandas as pd
import numpy as np

df_pedidos = pd.DataFrame({'Pedido_ID': [1, 2, 3, 4], 'Cliente_ID': [101, 102, 101, 103],
'Valor': [250, 400, 150, 600]})
df_clientes_end = pd.DataFrame({'Cliente_ID': [101, 102, 104], 'Cidade': ['São Paulo',
'Rio de Janeiro', 'Porto Alegre']})

pedidos_inner = pd.merge(df_pedidos, df_clientes_end, on='Cliente_ID', how='inner')
pedidos_left = pd.merge(df_pedidos, df_clientes_end, on='Cliente_ID', how='left', validate='many_to_one')

print(pedidos_inner)
print(f"Quantidade de linhas (inner): {len(pedidos_inner)}\n")
print(pedidos_left)
print(f"Quantidade de linhas (left): {len(pedidos_left)}")