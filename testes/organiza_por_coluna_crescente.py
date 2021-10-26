
from pandas import read_excel, DataFrame

df_medalhas = read_excel("bases/Medals.xlsx")


def soma_valores_por_linhas(df,*colunas):
    df["Total"] = 0
    for coluna in colunas:
        df["Total"] += df[coluna]
    return df

def organiza_por_coluna(df,coluna):
    return df.sort_values(coluna,ascending = False)

print("\nMedalhas totais de cada pais por Rank:\n",soma_valores_por_linhas(df_medalhas,"Gold","Silver","Bronze")[["Rank","Team/NOC","Total"]])


print(f"\nPaís com mais medalha de Ouro:\n {organiza_por_coluna(df_medalhas,'Gold').head(1)[['Team/NOC','Gold']]}")