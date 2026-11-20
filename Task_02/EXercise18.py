import pandas as pd

dados_func = {
    'Nome': [' ana silva ', 'CARLOS SOUZA', 'beatriz lima ', ' joão pedro'],
    'Cargo': [' Analista de Dados ', 'engenheiro de software', 'Cientista de Dados', '  analista de dados ']
}
df_func = pd.DataFrame(dados_func)

df_func['Nome'] = df_func['Nome'].str.strip().str.title()
df_func['Cargo'] = df_func['Cargo'].str.strip().str.lower()

qtd_analistas = int((df_func['Cargo'] == 'analista de dados').sum())

print(df_func)
print(f"\nQuantidade de funcionários com cargo 'analista de dados': {qtd_analistas}")