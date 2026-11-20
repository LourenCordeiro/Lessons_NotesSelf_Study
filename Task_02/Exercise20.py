import pandas as pd

dados_piv = {
    'Mes': ['Jan', 'Jan', 'Fev', 'Fev', 'Jan', 'Fev'],
    'Regiao': ['Norte', 'Sul', 'Norte', 'Sul', 'Norte', 'Sul'],
    'Produto': ['Smartphone', 'Smartphone', 'Notebook', 'Notebook', 'Tablet', 'Tablet'],
    'Vendas': [12000, 15000, 30000, 28000, 8000, 9500]
}
df_piv = pd.DataFrame(dados_piv)

vendas_produto_mes = pd.pivot_table(
    df_piv,
    index='Produto',
    columns='Mes',
    values='Vendas',
    aggfunc='sum',
    fill_value=0,
)
vendas_produto_mes = vendas_produto_mes[['Jan', 'Fev']]

vendas_notebook_fev = vendas_produto_mes.loc['Notebook', 'Fev']

print(vendas_produto_mes)
print(f"\nVendas de Notebook em Fevereiro: {vendas_notebook_fev}")