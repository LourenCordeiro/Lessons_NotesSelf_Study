import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(101)
cargos = np.random.choice(['Analista', 'Desenvolvedor', 'Gerente', 'Diretor'], 500)
salarios = np.where(
    cargos == 'Diretor', np.random.normal(25000, 4000, 500),
    np.where(
        cargos == 'Gerente', np.random.normal(12000, 2000, 500),
        np.where(
            cargos == 'Desenvolvedor', np.random.normal(8000, 1500, 500),
            np.random.normal(5000, 800, 500)
        )
    )
)

df_rh = pd.DataFrame({'Cargo': cargos, 'Salario': salarios})

plt.figure(figsize=(9, 5))
sns.boxplot(data=df_rh, x='Cargo', y='Salario')
plt.title('Distribuição Salarial por Cargo')
plt.xlabel('Cargo')
plt.ylabel('Salário (R$)')
plt.tight_layout()
plt.show()

sal_dev = df_rh.loc[df_rh['Cargo'] == 'Desenvolvedor', 'Salario']
q1 = sal_dev.quantile(0.25)
q3 = sal_dev.quantile(0.75)
iqr = q3 - q1
limite_superior = q3 + 1.5 * iqr
limite_inferior = q1 - 1.5 * iqr
outliers_superiores = sal_dev[sal_dev > limite_superior]

print(f"Quantidade de registros ('Desenvolvedor'): {len(sal_dev)}")
print(f"Q1 (25%): {q1:.2f}")
print(f"Q3 (75%): {q3:.2f}")
print(f"IQR (Q3 - Q1): {iqr:.2f}")
print(f"Limite superior (Q3 + 1.5 * IQR): {limite_superior:.2f}")
print(f"Limite inferior (Q1 - 1.5 * IQR): {limite_inferior:.2f}")
print(f"Outliers superiores detectados: {outliers_superiores.tolist()}")