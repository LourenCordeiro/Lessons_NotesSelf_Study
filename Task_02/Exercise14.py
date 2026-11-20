import numpy as pd
import pandas as pd

dados_acoes = {
'Data': ['2026-06-01', '2026-06-02', '2026-06-03', '2026-06-04', '2026-06-05'],
'Abertura': [100.5, 102.0, 101.5, 104.0, 103.5],
'Fechamento': [102.0, 101.0, 103.8, 103.2, 105.0]
}
df_acoes = pd.DataFrame(dados_acoes)
df_acoes['Data'] = pd.to_datetime(df_acoes['Data'])

df_acoes['Variacao_Diaria'] = (
    (df_acoes['Fechamento'] - df_acoes['Abertura']) / df_acoes['Abertura'] * 100
)

indice_maior_ganho = df_acoes['Variacao_Diaria'].idxmax()
dia_maior_ganho = df_acoes.loc[indice_maior_ganho]

print(df_acoes)
print(f"Dia com maior ganho: {dia_maior_ganho['Data']:%d/%m/%Y}: {dia_maior_ganho['Variacao_Diaria']:.2f}%")