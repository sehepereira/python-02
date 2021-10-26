from pandas import read_excel, DataFrame
df_atletas = read_excel("bases/Athletes.xlsx")
df_genero = read_excel("bases/EntriesGender.xlsx")
df_treinadores = read_excel("bases/Coaches.xlsx")
df_medalhas = read_excel("bases/Medals.xlsx")
df_times = read_excel("bases/Teams.xlsx")

def total_linhas(df):
    return len(df)

def conta_valores_de_uma_coluna(df,coluna):
    return sum(df[coluna])

#segundo parametro é a coluna que voce quer somar os dados e o terceiro é o dado que quer somar 
def organiza_e_soma_por_ondem(df,_organiza_coluna,_soma_coluna):
    grupo = df.groupby(_organiza_coluna)
    _a = grupo[[_soma_coluna,_organiza_coluna]].sum() # paises com mais medalhas
    return _a.sort_values(_soma_coluna, ascending = False)

def conta_quastas_vezes_aparece_o_nome_na_coluna(df,coluna):
    _i = DataFrame(df.value_counts(coluna)).rename(columns={0:'Total'}).reset_index(coluna)
    return _i

def soma_valores_por_linhas(df,*colunas):
    df["Total"] = 0
    for coluna in colunas:
        df["Total"] += df[coluna]
    return df

def organiza_por_coluna_crescente(df,coluna):
    return df.sort_values(coluna,ascending = False)

def organiza_por_coluna_decrescente(df,coluna):
    return df.sort_values(coluna,ascending = True)

def reseta_index(df):
    return df.reset_index().rename(columns={"index":'Index antigo'})
#segundo parametro é a coluna que voce quer somar os dados e o terceiro é o dado que quer somar 
def teste(df,*coluna):
    _i = df.loc[[coluna]]
    return _i

def conta_valores_duas_colunas(df,_coluna_depende,_coluna_agrupa,_coluna_count):
    grupo = df.groupby([_coluna_depende,_coluna_agrupa])
    _a = grupo[[_coluna_count]].count() 
    return _a.reset_index(_coluna_agrupa)
