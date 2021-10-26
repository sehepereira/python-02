from re import A
from flask import *
from tratamento_dados import *
from os import system as y

y("clear")

#atletas
#
#
#
#

#esporte
DataFrame(conta_quastas_vezes_aparece_o_nome_na_coluna(df=df_atletas,coluna='Discipline')).to_html('templates/esportes/quantidade_de_participantes_por_esporte.html')
DataFrame(conta_quastas_vezes_aparece_o_nome_na_coluna(df=df_atletas,coluna='Discipline')["Discipline"]).to_html('templates/esportes/esportes_participantes.html')
reseta_index(df_genero[df_genero['Male'] > df_genero["Female"]][["Discipline",'Male',"Female"]] ).to_html('templates/esportes/esportes_com_mais_homens_que_mulheres.html')
reseta_index(df_genero[df_genero['Male'] < df_genero["Female"]][["Discipline",'Male',"Female"]]).to_html('templates/esportes/esportes_com_mais_mulheres_que_homens.html')
conta_quastas_vezes_aparece_o_nome_na_coluna(df_treinadores,'Discipline').to_html('templates/esportes/quantidade_de_treinadores_por_esporte.html')

#pais
quantida_treinadors_pais = conta_quastas_vezes_aparece_o_nome_na_coluna(df_treinadores,'NOC')
quantida_treinadors_pais.head(1).to_html('templates/paises/pais_com_mais_treinadores.html')
quantida_treinadors_pais.to_html('templates/paises/quantidade_de_treinadores_por_pais.html')
conta_valores_duas_colunas(df_times,"NOC","Discipline","Event").to_html('templates/paises/quantidade_de_times_por_esporte_cada_pais_possui.html')

#medalhas
soma_valores_por_linhas(df_medalhas,"Gold","Silver","Bronze")[["Rank","Team/NOC","Total"]].to_html('templates/medalhas/total_de_medalhas_dos_pais.html')
organiza_por_coluna_crescente(soma_valores_por_linhas(df_medalhas,"Gold","Silver","Bronze")[["Rank","Team/NOC","Total"]], "Total").to_html('templates/medalhas/rank_de_melhadas_por_pais.html')
organiza_por_coluna_crescente(df_medalhas,'Gold').head(1)[['Team/NOC','Gold']].to_html('templates/medalhas/pais_com_mais_medalha_ouro.html')
organiza_por_coluna_crescente(df_medalhas,'Silver').head(1)[['Team/NOC','Silver']].to_html('templates/medalhas/pais_com_mais_medalha_prata.html')
organiza_por_coluna_crescente(df_medalhas,'Bronze').head(1)[['Team/NOC','Bronze']].to_html('templates/medalhas/pais_com_mais_medalha_bronze.html')
pais_com_menos_medalha_ouro = reseta_index(organiza_por_coluna_decrescente(df_medalhas,'Gold'))
pais_com_menos_medalha_ouro[pais_com_menos_medalha_ouro.loc[0,'Gold'] == pais_com_menos_medalha_ouro['Gold']].to_html('templates/medalhas/pais_com_menos_medalha_ouro.html',classes="asdasdasdsadsd")
pais_com_menos_medalha_prata = reseta_index(organiza_por_coluna_decrescente(df_medalhas,'Silver'))
pais_com_menos_medalha_prata[pais_com_menos_medalha_prata.loc[0,'Silver'] == pais_com_menos_medalha_prata['Silver']].to_html('templates/medalhas/pais_com_menos_medalha_prata.html')
pais_com_menos_medalha_bronze = reseta_index(organiza_por_coluna_decrescente(df_medalhas,'Bronze'))
pais_com_menos_medalha_bronze[pais_com_menos_medalha_bronze.loc[0,'Bronze'] == pais_com_menos_medalha_bronze['Bronze']].to_html('templates/medalhas/pais_com_menos_medalha_bronze.html')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', titulo_pagina='página inicial')

@app.route('/atletas/<subpath>')
def atletas(subpath):
    return render_template(f"atletas/{subpath}.html", titulo_pagina='Atletas', total_atletas=total_linhas(df_atletas), atletas_homens=conta_valores_de_uma_coluna(df=df_genero,coluna='Male'),atletas_mulheres=conta_valores_de_uma_coluna(df=df_genero,coluna='Female'), total_atletas_inscritos=(conta_valores_de_uma_coluna(df=df_genero,coluna='Female')+conta_valores_de_uma_coluna(df=df_genero,coluna='Male')))

@app.route('/esportes/<subpath>')
def esportes(subpath):
    return render_template(f'esportes/{subpath}.html', titulo_pagina='Sobre esportes')

@app.route('/medalhas/<subpath>')
def medalhas(subpath):
    return render_template(f'medalhas/{subpath}.html', titulo_pagina='Sobre medalhas')

@app.route('/paises/<subpath>')
def paises(subpath):
    return render_template(f'paises/{subpath}.html', titulo_pagina='Sobre paises')

@app.route('/graficos/<subpath>')
def graficos(subpath):
    return render_template(f'graficos/{subpath}.html', titulo_pagina='Sobre paises')

app.run(debug=True)




