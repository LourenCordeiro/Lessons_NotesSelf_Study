import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

np.random.seed(42)
n = 300
idade = np.random.randint(20, 75, n)
peso = np.random.uniform(50, 120, n)
colesterol = np.random.uniform(150, 300, n)
pressao = 70 + 0.4 * idade + 0.3 * peso + 0.1 * colesterol + np.random.normal(0, 5, n)

df_saude = pd.DataFrame({
    'Idade': idade,
    'Peso': peso,
    'Colesterol': colesterol,
    'Pressao_Sistolica': pressao
})

matriz_corr = df_saude.corr(method='pearson')

plt.figure(figsize=(7, 5))
sns.heatmap(
    matriz_corr,
    annot=True,
    fmt='.2f',
    cmap='coolwarm',
    center=0,
    vmin=-1,
    vmax=1
)
plt.title('Matriz de Correlação de Pearson — Dados de Saúde')
plt.tight_layout()
plt.show()

correlacoes_pressao = matriz_corr['Pressao_Sistolica'].drop('Pressao_Sistolica')
variavel_maior_corr = correlacoes_pressao.idxmax()
valor_maior_corr = float(correlacoes_pressao.max())

print("--- Matriz de Correlação de Pearson ---")
print(matriz_corr.round(4))
print("\n--- Correlações com Pressao_Sistolica (ordem decrescente) ---")
print(correlacoes_pressao.sort_values(ascending=False).round(4))
print(f"\nMaior correlação com Pressao_Sistolica: {variavel_maior_corr} (r = {valor_maior_corr:.4f})")