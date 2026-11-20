import pandas as pd

dados_fastfood = {
'Filial': ['Centro', 'Centro', 'Sul', 'Sul', 'Centro', 'Sul', 'Norte', 'Norte'],
'Categoria': ['Bebida', 'Lanche', 'Lanche', 'Sobremesa', 'Bebida', 'Sobremesa',
'Lanche', 'Bebida'],
'Valor_Venda': [15.0, 45.0, 48.0, 20.0, 12.0, 18.0, 50.0, 14.0]
}
df_ff = pd.DataFrame(dados_fastfood)

agrupado_ff = df_ff.groupby(['Filial', 'Categoria'])['Valor_Venda'].agg(['sum', 'mean'])

soma_centro = df_ff.loc[df_ff['Filial'] == 'Centro', 'Valor_Venda'].sum()
soma_centro_via_agg = agrupado_ff.loc['Centro', 'sum'].sum()

print(agrupado_ff)
print(f"\nSoma total de vendas na filial 'Centro': {soma_centro:.1f}")
print(f"Conferência via tabela agrupada: {soma_centro_via_agg:.1f}")