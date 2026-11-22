import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

np.random.seed(123)
n = 200
renda = np.random.uniform(20, 140, n)
gasto = np.random.uniform(10, 100, n)
cluster = np.random.choice(['Conservador', 'Moderado', 'Extrovertido'], n)

df_clientes = pd.DataFrame({
    'Renda_Anual': renda,
    'Score_Gasto': gasto,
    'Perfil': cluster
})

plt.figure(figsize=(9, 5))
sns.scatterplot(
    data=df_clientes,
    x='Renda_Anual',
    y='Score_Gasto',
    hue='Perfil',
    alpha=0.8
)
plt.title('Segmentação de Clientes: Renda Anual vs. Score de Gasto por Perfil')
plt.xlabel('Renda Anual (mil R$)')
plt.ylabel('Score de Gasto')
plt.legend(title='Perfil')
plt.tight_layout()
plt.show()

media_score_por_perfil = (
    df_clientes.groupby('Perfil')['Score_Gasto']
    .mean()
    .sort_values(ascending=False)
)

perfil_maior_media = media_score_por_perfil.idxmax()
maior_media_valor = float(media_score_por_perfil.max())

print("--- Média de Score_Gasto por Perfil ---")
print(media_score_por_perfil.round(4))
print(
    f"\nPerfil com maior média de Score_Gasto: {perfil_maior_media} "
    f"({maior_media_valor:.4f})"
)