import time
import numpy as np

rng = np.random.default_rng(seed=42)

distancias_km = rng.uniform(low=50.0, high=1000.0, size=100_000)
precos_combustivel = rng.normal(loc=5.80, scale=0.45, size=100_000)

t0_loop = time.perf_counter()
custos_loop = []
for d, p in zip(distancias_km, precos_combustivel):
    custo_i = (float(d) / 12.0) * float(p)
    custos_loop.append(custo_i)
total_loop = sum(custos_loop)
t1_loop = time.perf_counter()
tempo_loop = t1_loop - t0_loop

t0_vec = time.perf_counter()
custos_vec = (distancias_km / 12.0) * precos_combustivel
total_vec = float(np.sum(custos_vec))
t1_vec = time.perf_counter()
tempo_vec = t1_vec - t0_vec

veiculos_acima_350 = custos_vec[custos_vec > 350.0]
qtd_acima_350 = int(veiculos_acima_350.size)


fator_mais_rapido = tempo_loop / tempo_vec

print(f"Total via loop Python:   R$ {total_loop:,.2f} | Tempo: {tempo_loop * 1000:.3f} ms")
print(f"Total vetorizado NumPy:  R$ {total_vec:,.2f} | Tempo: {tempo_vec * 1000:.3f} ms")
print(f"NumPy foi ~{fator_mais_rapido:.1f}x mais rápido que o loop iterativo")
print(f"Veículos com custo > R$ 350,00: {qtd_acima_350}")