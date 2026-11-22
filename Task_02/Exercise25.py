import pandas as pd
import numpy as np

rng = np.random.default_rng(seed=42)

valores_exp = rng.exponential(scale=100.0, size=10_000)
df_tx = pd.DataFrame({'Transacao_Valor': valores_exp})

resumo = df_tx['Transacao_Valor'].describe()

assimetria = df_tx['Transacao_Valor'].skew()
curtose = df_tx['Transacao_Valor'].kurt()

print("--- Estatísticas Descritivas ---")
print(resumo)
print(f"\nAssimetria (skew): {assimetria:.4f}")
print(f"Curtose em excesso (kurt): {curtose:.4f}")
print(f"Mediana (50%): {resumo['50%']:.4f} | Média: {resumo['mean']:.4f}")
print("Mediana < Média?", resumo['50%'] < resumo['mean'])