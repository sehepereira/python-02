from pandas import read_excel, DataFrame

df_medalhas = read_excel("bases/Medals.xlsx")


def organiza_por_coluna_decrescente(df,coluna):
    return DataFrame(df.sort_values(coluna,ascending = True))

pais_com_menos_medalha_ouro = organiza_por_coluna_decrescente(df_medalhas,'Gold').reset_index().rename(columns={"index":'Index antigo'})
print(f"\nPaís com menos medalha de Ouro:\n {pais_com_menos_medalha_ouro[pais_com_menos_medalha_ouro.loc[0,'Gold'] == pais_com_menos_medalha_ouro['Gold']]}")

