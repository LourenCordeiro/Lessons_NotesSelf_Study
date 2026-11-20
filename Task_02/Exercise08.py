import numpy as np

#Inicialização de um gerador pseudoaleatório moderno com semente para reprodutibilidade
rng = np.random.default_rng(seed=42)

#Geração das coordenadas 
clientes = rng.random((100_000, 2))
centros = rng.random((5, 2))

#Cálculo das diferenças entre os clientes e os centros de atendimento
diferencas = clientes[:, None, :] - centros[None, :, :]

#Cálculo das distâncias euclidianas
distancias = np.linalg.norm(diferencas, axis=-1)

#Encontrar o centro de atendimento mais próximo para cada cliente
menor_distancia_cliente_0 = np.min(distancias[0])
indice_centro_mais_proximo = np.argmin(distancias[0])

print(f"Shape da matriz de distâncias: {distancias.shape}")
print(f"Menor distância do cliente 0: {menor_distancia_cliente_0:.6f}")
print(f"Centro mais próximo do cliente 0 (índice): {indice_centro_mais_proximo}")