import pandas as pd

# 1. Criação do dicionário com o histórico de empréstimos
dados_emprestimos = {
    'Cliente_ID': [201, 202, 203, 204, 205, 206, 207, 208, 209, 210],
    'Score_Credito': [620, 750, 510, 800, 480, 590, 710, 650, 430, 720],
    'Valor_Solicitado': [10000, 25000, 5000, 50000, 3000, 15000, 30000, 20000, 2000, 35000],
    'Renda_Mensal': [3500, 9000, 2200, 15000, 1800, 3000, 8500, 6000, 1500, 9500],
    'Inadimplente': [0, 0, 1, 0, 1, 1, 0, 0, 1, 0] 
}
df_emp = pd.DataFrame(dados_emprestimos)

desc = df_emp.describe()
media_score = desc.loc['mean', 'Score_Credito']
mediana_score = desc.loc['50%', 'Score_Credito']
diff_score = media_score - mediana_score

renda_por_status = df_emp.groupby('Inadimplente')['Renda_Mensal'].mean()

df_emp['Comp_Renda'] = df_emp['Valor_Solicitado'] / df_emp['Renda_Mensal']
idx_max_comp = df_emp['Comp_Renda'].idxmax()
cliente_max_comp = int(df_emp.loc[idx_max_comp, 'Cliente_ID'])
max_comp_valor = float(df_emp.loc[idx_max_comp, 'Comp_Renda'])

print("--- Resumo Estatístico ---")
print(desc)
print(
    f"\nScore_Credito -> Média: {media_score:.2f} | "
    f"Mediana (50%): {mediana_score:.2f} | "
    f"Diferença (Média - Mediana): {diff_score:.2f}"
)

print("\n--- Renda_Mensal Média por Status (0 = Adimplente, 1 = Inadimplente) ---")
print(renda_por_status)

print("\n--- Proporção Valor_Solicitado / Renda_Mensal (Comp_Renda) ---")
print(df_emp[['Cliente_ID', 'Valor_Solicitado', 'Renda_Mensal', 'Comp_Renda', 'Inadimplente']])
print(f"\nMaior razão (Comp_Renda): {max_comp_valor:.2f}x (Cliente_ID: {cliente_max_comp})")