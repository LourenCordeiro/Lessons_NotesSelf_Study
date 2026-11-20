import numpy as np

#Inicializa o gerador pseudoaleatório com semente para reprodutibilidade
rng = np.random.default_rng(seed=42)

#Cria uma matriz 2000 x 50 com valores aleatórios uniformes no intervalo [10, 500)
X = rng.uniform(low=10.0, high=500.0, size=(2000, 50))

#Calcula o mínimo e o máximo de cada coluna (axis=0) -> shape (50,)
X_min = np.min(X, axis=0)
X_max = np.max(X, axis=0)

#Aplica a normalização Min-Max vetorizada sem loops -> shape (2000, 50)
X_norm = (X - X_min) / (X_max - X_min)

# Calcula a soma total de todos os elementos da matriz normalizada
soma_total = np.sum(X_norm)

print(f"Shape da matriz normalizada: {X_norm.shape}")
print(f"Mínimo global após normalização: {np.min(X_norm):.4f}")
print(f"Máximo global após normalização: {np.max(X_norm):.4f}")
print(f"Soma total dos valores após normalização: {soma_total:.4f}")