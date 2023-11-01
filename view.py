import pandas as pd
import sqlite3 as lite

from datetime import datetime, date
from math import floor

import os

#criando conexao
con = lite.connect('lar.db')

def inserir_infos(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO cadastro_acolhidos(nome, data_nascimento, idade, cor_raca, data_acolhimento, PIA, n_guiaAcolhimento, n_processo, situacao_juridica, municipio, motivo_acolhimento, ano, escola, curso_prof) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
        cur.execute(query,i)

def atualizar_infos(i):
    with con:
        cur = con.cursor()
        query = '''UPDATE cadastro_acolhidos
                   SET nome=?, data_nascimento=?, idade=?, cor_raca=?, data_acolhimento=?, PIA=?, n_guiaAcolhimento=?, n_processo=?, situacao_juridica=?, municipio=?, motivo_acolhimento=?, ano=?, escola=?, curso_prof=?
                   WHERE id_interno=?'''
        cur.execute(query,i)

def mostrar_infos():
    
    with con:
        lista = []
        cur = con.cursor()
        query = "SELECT * FROM cadastro_acolhidos"
        cur.execute(query)
        info = cur.fetchall()
        
        for i in info:
            lista.append(i)
    return lista

def deletar_infos(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM cadastro_acolhidos WHERE id_interno=?"
        cur.execute(query,i)

def calcular_idade(e_nasc):
    
    e_nasc = e_nasc.get()

    data_nascimento = datetime.strptime(e_nasc, "%d/%m/%Y").date()
    hoje = date.today()
    dias_vividos = (hoje - data_nascimento).days
    idade = floor(dias_vividos / 365.25)
    return idade

def exportar_infos():
    df = pd.read_sql_query("SELECT * FROM cadastro_acolhidos", con)
    downloads_path = os.path.join(os.path.expanduser('~'), 'downloads')
    arquivo = os.path.join(downloads_path, 'tabela_lar.xlsx')
    df.to_excel(arquivo, index=False)