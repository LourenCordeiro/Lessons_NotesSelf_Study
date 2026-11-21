import pandas as pd

df_sem1 = pd.DataFrame({'Mes': ['Jan', 'Fev', 'Mar'], 'Livros_Vendidos': [150, 200, 180]})
df_sem2 = pd.DataFrame({'Mes': ['Jul', 'Ago', 'Set'], 'Livros_Vendidos': [220, 310, 290]})

df_vendas_ano = pd.concat([df_sem1, df_sem2], ignore_index=True)

df_anual = pd.concat([df_sem1, df_sem2], axis=0, ignore_index=True)

total_livros = int(df_anual['Livros_Vendidos'].sum())

print(df_anual)
print(f"\nTotal de livros vendidos(Acumulado): {total_livros}")

