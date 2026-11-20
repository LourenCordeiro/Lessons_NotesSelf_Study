import pandas as pd
import numpy as np

dados_usuarios = {
'Usuario': ['Alice', 'Bruno', 'Carla', 'Daniel', 'Eva'],
'Acessos_Mes': [2, 15, 28, 8, 45]
}
df_users = pd.DataFrame(dados_usuarios)

condicoes = [
    df_users['Acessos_Mes'] < 5,
    (df_users['Acessos_Mes'] >= 5) & (df_users['Acessos_Mes'] <= 20),
    df_users['Acessos_Mes'] > 20
]
escolhas = ['Baixo', 'Médio', 'Alto']

df_users['Nível'] = np.select(condicoes, escolhas, default='Indefinido')

qtd_alto = int((df_users['Nível'] == 'Alto').sum())

print(df_users)
print(f"\nQuantidade de usuários na categoria 'Alto': {qtd_alto}")