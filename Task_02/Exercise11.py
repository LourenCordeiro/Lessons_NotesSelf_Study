import numpy as np

rng = np.random.default_rng(seed=42)
rng = np.random.default_rng(seed=42)


salinidade = rng.random(size=(500, 500))

suavizada = salinidade.copy()
suavizada[1:-1, 1:-1] = (
    salinidade[:-2, :-2]  + salinidade[:-2, 1:-1]  + salinidade[:-2, 2:]
    + salinidade[1:-1, :-2] + salinidade[1:-1, 1:-1] + salinidade[1:-1, 2:]
    + salinidade[2:, :-2]   + salinidade[2:, 1:-1]   + salinidade[2:, 2:]
) / 9


print(f" Sanilidade antes da suavização: {salinidade[250, 250]:.4f}") 
print(f" Sanilidade após a suavização: {suavizada[250, 250]:.4f}") 
