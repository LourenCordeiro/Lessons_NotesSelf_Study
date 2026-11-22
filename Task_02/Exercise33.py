import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.ticker import FuncFormatter

np.random.seed(7)
datas = pd.date_range(start='2026-01-01', periods=90, freq='D')
faturamento = 50000 + 10000 * np.sin(np.linspace(0, 3 * np.pi, 90)) + np.random.normal(0, 3000, 90)
df_vendas_diarias = pd.DataFrame({'Data': datas, 'Faturamento': faturamento})

df_vendas_diarias = df_vendas_diarias.set_index('Data')
faturamento_semanal = df_vendas_diarias['Faturamento'].resample('W').mean()
media_geral = df_vendas_diarias['Faturamento'].mean()

data_pico = faturamento_semanal.idxmax()
semana_pico = data_pico.isocalendar().week

fig, ax = plt.subplots(figsize=(10, 5))

ax.plot(faturamento_semanal.index, faturamento_semanal.values,
        color='#2a78d6', linewidth=2, marker='o', markersize=6, label='Média semanal')
ax.axhline(media_geral, color='#52514e', linestyle='--', linewidth=1.5,
           label=f'Média do período (R$ {media_geral:,.0f})')
ax.annotate(f'Pico: semana {semana_pico} (R$ {faturamento_semanal.max():,.0f})',
            xy=(data_pico, faturamento_semanal.max()),
            xytext=(0, 10), textcoords='offset points', ha='center', va='bottom')

ax.set_title('Faturamento médio semanal — 1º trimestre de 2026', loc='left', fontsize=13)
ax.set_xlabel('Semana (data de fechamento, domingo)')
ax.set_ylabel('Faturamento médio diário (R$)')
ax.yaxis.set_major_formatter(FuncFormatter(lambda valor, _: f'R$ {valor:,.0f}'))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m'))
ax.set_ylim(top=63000)
ax.grid(axis='y', color='#e5e4e0', linewidth=0.8)
ax.spines[['top', 'right']].set_visible(False)
ax.legend(frameon=False, loc='lower left')

plt.tight_layout()
plt.show()

print(faturamento_semanal.round(2))
print(f"Pico: semana {semana_pico}, encerrada em {data_pico:%d/%m/%Y}")