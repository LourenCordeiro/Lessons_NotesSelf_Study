import pandas as pd

dados_chamados = {
    'Chamado_ID': [1, 2, 3, 4],
    'Data_Abertura': [
        '2026-06-01 08:30:00',
        '2026-06-02 14:15:00',
        '2026-06-03 09:00:00',
        '2026-06-06 18:45:00'
    ]
}
df_cham = pd.DataFrame(dados_chamados)
df_cham['Data_Abertura'] = pd.to_datetime(df_cham['Data_Abertura'])

df_cham['Dia_Semana'] = df_cham['Data_Abertura'].dt.day_name()
df_cham['Dia_Semana_Num'] = df_cham['Data_Abertura'].dt.dayofweek
df_cham['Hora'] = df_cham['Data_Abertura'].dt.hour

hora_chamado_4 = int(df_cham.loc[df_cham['Chamado_ID'] == 4, 'Hora'].iloc[0])

print(df_cham)
print(f"\nHora do dia em que o chamado de ID 4 foi aberto: {hora_chamado_4}")