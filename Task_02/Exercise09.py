import numpy as np

#Simulação de monte carlo e retornos compostos
rng = np.random.default_rng(seed=42)

#Parâmetros da simulação
n_dias = 252
n_simulacoes = 1000
preco_inicial = 100
media_retorno = 0.0005
desvio_retorno = 0.02

#Array 2D (252, 1000) de retornos diários N (0.0005, 0.02)
retornos = rng.normal(loc=media_retorno, scale=desvio_retorno, size=(n_dias, n_simulacoes))

#fatores de multiplicação para cada simulação
fatores = 1.0 + retornos
precos_fechamento = preco_inicial * np.cumprod(fatores, axis=0)

#Valor máximo no último dia(252)
maximo_dia_252 = np.max(precos_fechamento[-1])
indice_sim_maxima = np.argmax(precos_fechamento[1])

print(f"Shape da matriz de preços: {precos_fechamento.shape}")
print(f"Maior preço no dia 252: ${maximo_dia_252:.2f}")
print(f"Simulação com o maior preço no dia 252 (índice): {indice_sim_maxima}")