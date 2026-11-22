import pandas as pd
import numpy as np

rng = np.random.default_rng(seed=42)
retornos_simulados = rng.normal(loc=0.0008, scale=0.015, size=(100, 3))

df_retornos = pd.DataFrame(retornos_simulados, columns=['Acao_A', 'Acao_B', 'Acao_C'])

cov_matrix = df_retornos.cov()

pesos = np.array([0.4, 0.4, 0.2])
variancia_carteira = float(pesos.T @ cov_matrix.to_numpy() @ pesos)
volatilidade_carteira = float(np.sqrt(variancia_carteira))

print("--- Matriz de Covariância ---")
print(cov_matrix)
print(f"\nVariância da carteira: {variancia_carteira:.8f}")
print(
    f"Volatilidade (desvio padrão) da carteira: "
    f"{volatilidade_carteira:.6f} ({volatilidade_carteira * 100:.4f}%)"
)