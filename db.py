import sqlite3 as lite

con = lite.connect('lar.db')

with con:
    c = con.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS cadastro_acolhidos( id_interno INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, data_nascimento DATE, idade INTGER, cor_raca TEXT, data_acolhimento DATE, PIA TEXT, n_guiaAcolhimento INTEGER, n_processo INTEGER, situacao_juridica TEXT, municipio TEXT, motivo_acolhimento TEXT, ano TEXT, escola TEXT, curso_prof TEXT)')
