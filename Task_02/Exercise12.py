import pandas as pd
import numpy as np

#Criação do dicionário com as informações dos clientes
dados_clientes = {
    'Cliente_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Idade': [22, 35, 45, 29, 52, 23, 41, 38, 60, 27],
    'Gasto_Anual': [1200.5, 4500.0, 8900.2, 3100.0, 12000.0, 950.0, 5400.0, 4800.0, 15000.0, 2200.0],
    'Cancelou': [0, 0, 1, 0, 1, 1, 0, 0, 1, 0]
}

#Criação do DataFrame com os dados dos clientes
df_clientes = pd.DataFrame(dados_clientes)

#Cálculo do gasto médio por status
gasto_medio_por_status = df_clientes.groupby('Cancelou')['Gasto_Anual'].mean()

#Cálculo do gasto médio por status ativos e cancelados
gasto_medio_ativos = gasto_medio_por_status.loc[0]
gasto_medio_cancelados = gasto_medio_por_status.loc[1]

#Cálculo da diferença percentual entre o gasto médio de cancelados e ativos
diferenca_percentual = (gasto_medio_cancelados - gasto_medio_ativos) / gasto_medio_ativos * 100

print(f"Gasto médio por status: {gasto_medio_por_status}")
print()
print(f"Diferença percentual entre o gasto médio de cancelados e ativos: {diferenca_percentual:.2f}%")