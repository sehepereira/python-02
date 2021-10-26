from pandas import read_excel, DataFrame
from os import system

system("clear")

def conta_quastas_vezes_aparece_o_nome_na_couna(df,coluna):
    _i = DataFrame(df.value_counts(coluna)).rename(columns={0:'Total'}).reset_index(coluna)
    return _i

df1 = read_excel("bases/Athletes.xlsx")
df2 = read_excel("bases/EntriesGender.xlsx")

print("DF 1 atletas")
print(conta_quastas_vezes_aparece_o_nome_na_couna(df1,"Discipline"))



def total_linhas_por_coluna(df,coluna):
    return sum(df[coluna])
    

def soma_valores_por_linha_de_duas_colunas(df,coluna1,coluna2):
    df["Total"] = (df[coluna1] + df[coluna2])
    return df.sort_values("Total",ascending = False)

print("\n\nDF 2 Sexo por inscrição")

print(soma_valores_por_linha_de_duas_colunas(df2,"Female","Male"))