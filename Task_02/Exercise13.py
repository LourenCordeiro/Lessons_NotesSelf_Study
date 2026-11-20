import numpy as np
import pandas as pd

dados_vendas = {
'Produto': ['Teclado', 'Mouse', 'Monitor', 'Cadeira', 'Headset', 'Webcam'],
'Preco': [150.0, np.nan, 1200.0, 850.0, np.nan, 300.0],
'Qtd_Vendida': [45, 120, 30, np.nan, 80, 55]
}

df_vendas = pd.DataFrame(dados_vendas)

#Cálculo do número de linhas com valores nulos
linhas_com_nulos = df_vendas.isna().any(axis=1).sum()

#Cálculo da mediana do preço
mediana_preco = df_vendas['Preco'].median()
df_vendas_limpo = df_vendas.fillna({'Preco': mediana_preco, 'Qtd_Vendida': 10})

#Cálculo do faturamento por produto
df_vendas_limpo['Faturamento'] = df_vendas_limpo['Preco'] * df_vendas_limpo['Qtd_Vendida']


faturamento_por_produto = (
    df_vendas_limpo.groupby('Produto')['Faturamento']
    .sum()
    .sort_values(ascending=False)
)
produto_maior_receita = faturamento_por_produto.idxmax()

print(f"Número de linhas com valores nulos: {linhas_com_nulos}")
print(f"Faturamento por produto: {faturamento_por_produto}")
print(f"Produto com maior receita: {produto_maior_receita}")