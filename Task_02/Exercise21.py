import pandas as pd
import numpy as np

dados_logs = {
'IP': ['192.168.1.1', '10.0.0.5', '192.168.1.1', '172.16.0.4', '10.0.0.5'],
'Acao': ['Login', 'Logout', 'Login', 'Erro', 'Logout'],
'Status': [200, 200, 200, 500, 200]
}
df_logs = pd.DataFrame(dados_logs)

qtd_duplicatas = int(df_logs.duplicated(keep='first').sum())

df_limpo = df_logs.drop_duplicates(keep='last')

print(f"Quantidade de linhas duplicadas: {qtd_duplicatas}")
print(f"Quantidade de linhas restantes: {len(df_limpo)}")