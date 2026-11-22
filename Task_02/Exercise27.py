import numpy as np
import pandas as pd

# 1. Gerador pseudoaleatório moderno com semente para reprodutibilidade
rng = np.random.default_rng(seed=42)

# 2. Geração de 1000 leituras x 3 sensores (Temperatura, Umidade, Pressao) e empilhamento em matriz 1000 x 3
temperatura = rng.normal(loc=72.0, scale=6.0, size=1000)
umidade = rng.normal(loc=55.0, scale=8.0, size=1000)
pressao = rng.normal(loc=4.2, scale=0.6, size=1000)

dados_sensores = np.column_stack([temperatura, umidade, pressao])  # shape: (1000, 3)

# 3. Conversão para DataFrame Pandas
df_sensores = pd.DataFrame(
    dados_sensores,
    columns=['Temperatura', 'Umidade', 'Pressao']
)

# 4. Simulação de turnos operacionais e adição da coluna condicional de status de alerta
df_sensores['Turno'] = rng.choice(['Manha', 'Tarde', 'Noite'], size=1000)

condicoes = [
    (df_sensores['Temperatura'] > 85.0) | (df_sensores['Pressao'] > 5.5),
    (df_sensores['Temperatura'] > 78.0) | (df_sensores['Pressao'] > 4.9) | (df_sensores['Umidade'] > 70.0)
]
escolhas = ['Critico', 'Alerta']

df_sensores['Status_Alerta'] = np.select(condicoes, escolhas, default='Normal')

# 5. Média agrupada por turno e contagem de ocorrências por status de alerta
media_por_turno = df_sensores.groupby('Turno')[['Temperatura', 'Umidade', 'Pressao']].mean()
contagem_status = df_sensores['Status_Alerta'].value_counts()
status_predominante = contagem_status.idxmax()

print("--- Média por Turno ---")
print(media_por_turno)
print("\n--- Distribuição de Status_Alerta ---")
print(contagem_status)
print(f"\nStatus predominante na linha de produção: {status_predominante}")