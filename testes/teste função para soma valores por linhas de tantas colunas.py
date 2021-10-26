from pandas import read_excel
from os import system as y
y("clear")
df_medalhas = read_excel("bases/Medals.xlsx")
df2 = read_excel("bases/EntriesGender.xlsx")

def soma_valores_por_linhas(df,*colunas):
    df["Total"] = 0
    for coluna in colunas:
        df["Total"] += df[coluna]
    return df.sort_values("Total",ascending = False)
print(soma_valores_por_linhas(df_medalhas,"Gold","Silver","Bronze").head(3))


def soma_valores_por_linha_de_duas_colunas(df,coluna1,coluna2,coluna3):
    df["Total"] = (df[coluna1] + df[coluna2] + df[coluna3])
    return df.sort_values("Total",ascending = False)
print(soma_valores_por_linha_de_duas_colunas(df_medalhas,"Gold","Silver","Bronze").head(3))



