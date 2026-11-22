import pandas as pd

dados_transacoes = {
    'Transacao_ID': [501, 502, 503, 504, 505, 506, 507, 508, 509, 510],
    'Canal': ['App', 'Web', 'App', 'POS', 'Web', 'POS', 'App', 'Web', 'POS', 'App'],
    'Valor_Transacao': [120.0, 4500.0, 85.0, 350.0, 15000.0, 45.0, 290.0, 5200.0, 95.0, 150.0],
    'Pais_Origem': ['Brasil', 'Brasil', 'Brasil', 'EUA', 'Rússia', 'Brasil', 'Brasil', 'Brasil', 'EUA', 'Brasil'],
    'Fraude': [0, 0, 0, 0, 1, 0, 0, 1, 0, 0] 
}
df_tx = pd.DataFrame(dados_transacoes)

desc = df_tx.describe()

total_por_pais = df_tx.groupby('Pais_Origem')['Valor_Transacao'].sum()
pais_maior_volume = total_por_pais.idxmax()

fraudes = df_tx[df_tx['Fraude'] == 1]
canais_fraude = fraudes['Canal'].value_counts()
canal_predominante_fraude = canais_fraude.idxmax()


print(desc)
print("\n--- Valor Total Movimentado por País (Pais_Origem) ---")
print(total_por_pais)
print(
    f"\nPaís com maior volume financeiro: {pais_maior_volume} "
    f"({total_por_pais[pais_maior_volume]:.1f})"
)
print("\n--- Transações Marcadas como Fraude (Fraude == 1) ---")
print(fraudes)
print("\n--- Frequência de Canal nas Fraudes ---")
print(canais_fraude)
print(f"\nCanal predominante nas fraudes: {canal_predominante_fraude}")