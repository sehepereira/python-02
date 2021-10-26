import os
from pandas import read_excel, DataFrame

df_times = read_excel("bases/Teams.xlsx")



def conta_quastas_vezes_aparece_o_nome_na_couna(df,coluna):
    _i = DataFrame(df.value_counts(coluna)).rename(columns={0:'Total'}).reset_index(coluna)
    return _i


def organiza_por_coluna_decrescente(df,coluna):
    return df.sort_values(coluna,ascending = True)

def organiza_e_soma_por_ondem(df,_organiza_coluna,_soma_coluna,coluna):
    grupo = df.groupby(_organiza_coluna)
    _a = grupo[[_soma_coluna,_organiza_coluna]].sum# paises com mais medalhas
    return DataFrame(_a)

print()


def conta_quastas_vezes_aparece_o_nome_na_couna(df,*coluna):
    _i = DataFrame(df.value_counts(coluna)).rename(columns={0:'Total'}).reset_index(coluna)
    return _i

os.system("clear")
grupo_esportes = df_times.groupby(['NOC','Discipline'])
dados_melhores_paises = grupo_esportes[['Event']].count()
print(dados_melhores_paises.reset_index('Discipline'))