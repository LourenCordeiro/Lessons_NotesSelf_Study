import pandas as pd
import numpy as np

dados_corp = {
'Pais': ['Brasil', 'Brasil', 'Argentina', 'Argentina', 'Brasil'],
'Filial': ['SP', 'RJ', 'BA', 'Mendoza', 'MG'],
'Faturamento': [50000, 30000, 20000, 15000, 40000]
}
df_corp = pd.DataFrame(dados_corp)

df_ordenado = df_corp.sort_values(
    by=['Pais', 'Faturamento'],
    ascending=[True, False]
)

primeira_filial = df_ordenado.iloc[0]['Filial']

print(df_ordenado)
print(f"Filial na primeira linha: {primeira_filial}")