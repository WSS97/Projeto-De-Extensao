from tkinter import *
from tkinter import font
from tkcalendar import Calendar, DateEntry
from tkinter import ttk
from view import *
from tkinter import messagebox


#cores:

co1 = "#feffff" #ciano
co2 = "#4fa882" #green

# listas utilizadas em botoes
list_corRaca = ["Preto", "Pardo", "Branco","Amarelo","Indigena"]
list_pia=["De acorodo com normativa","Divergente de normativa", "Não possui"]
list_situacaoJuridica=["Destituido", "Em processo de adocao", "Sem processo", "Em processo de medida protetiva"]
list_motivoAcolhimento=["Negligência familiar", "Abandono", "Violência sexual", "Agressão fisica", "Genitores ou responsaveis vitmas de violência", "Falecimento de genitores ou  responsaveis"]
list_sn = ["Sim","Não"]

janela = Tk()
janela.title()
janela.geometry('1080x600')
janela.configure(background="#e9edf5")
janela.resizable(width=FALSE, height=FALSE)

# frames divisorios
frame_cima = Frame(janela, width=400, height=50, bg=co2, relief='flat')
frame_cima.grid(row=0, column=0)

frame_baixo = Frame(janela, width=400, height=550, bg='#dbead5', relief='flat')
frame_baixo.grid(row=1, column=0, padx=0, pady=1, sticky=NSEW)

frame_meio = Frame(janela, width=400, height=50, bg=co2, relief='flat')
frame_meio.place(x=0, y=330)

frame_direita = Frame(janela, width=660, height=540, bg='#E9EDF5', relief='flat')
frame_direita.grid(row=0, column=1, rowspan=2, padx=1, pady=0, sticky=NSEW)

#label cima
app_name = Label(frame_cima, text='Acolhido(s)', anchor=NW, font=('Ivy 13 bold'), bg=co2, fg=co1, relief='flat')
app_name.place(x=10, y=20)


#variavel global
global linha_1

#funcao inserir(cadastrar)
def inserir():
    nome = e_name.get()
    data_nascimento = e_nasc.get()
    cor_raca = e_corRaca.get()
    data_acolhimento = e_dataAcolhimento.get()
    PIA = e_pia.get()
    n_guiaAcolhimento = e_n_guiaAcolhimento.get()
    situacao_juridica = e_situacaoJuridica.get()
    municipio = e_municipio.get()
    n_processo = e_n_processo.get()
    motivo_acolhimento = e_motivoAcolhimento.get()
    escola = e_escola.get()
    ano = e_ano.get()
    curso_prof = e_cursoProf.get()
    idade = calcular_idade(e_nasc)

    lista = [nome, data_nascimento, idade, cor_raca, data_acolhimento, PIA, n_guiaAcolhimento, n_processo, situacao_juridica, municipio, motivo_acolhimento, ano, escola, curso_prof]

    if nome == '' or n_guiaAcolhimento == '' or n_processo == '':
        messagebox.showerror('Erro.','* indica um campo obrigatorio \n Existe(m) campo(s) obrigatorio(s) em vazio!')
    else:
        inserir_infos(lista)
        messagebox.showinfo('Dados cadastrados com sucesso!')

        e_name.delete(0,'end')
        e_nasc.delete(0,'end')
        e_corRaca.delete(0,'end')
        e_dataAcolhimento.delete(0,'end')
        e_pia.delete(0,'end')
        e_n_guiaAcolhimento.delete(0,'end')
        e_situacaoJuridica.delete(0,'end')
        e_municipio.delete(0,'end')
        e_n_processo.delete(0,'end')
        e_motivoAcolhimento.delete(0,'end')
        e_escola.delete(0,'end')
        e_ano.delete(0,'end')
        e_cursoProf.delete(0,'end')

        for widget in frame_direita.winfo_children():
            widget.destroy()

        display()


# função atualizar
def atualizar():
    try:
        treev_dados = linha_1.focus()
        treev_dicionario = linha_1.item(treev_dados)
        tree_lista = treev_dicionario['values']

        id_interno = tree_lista[0]

        e_name.delete(0,'end')
        e_nasc.delete(0,'end')
        e_corRaca.delete(0,'end')
        e_dataAcolhimento.delete(0,'end')
        e_pia.delete(0,'end')
        e_n_guiaAcolhimento.delete(0,'end')
        e_situacaoJuridica.delete(0,'end')
        e_municipio.delete(0,'end')
        e_n_processo.delete(0,'end')
        e_motivoAcolhimento.delete(0,'end')
        e_escola.delete(0,'end')
        e_ano.delete(0,'end')
        e_cursoProf.delete(0,'end')  



        e_name.insert(0, tree_lista[1])
        e_nasc.insert(0, tree_lista[2])
        e_corRaca.insert(0, tree_lista[4])
        e_dataAcolhimento.insert(0, tree_lista[5])
        e_pia.insert(0, tree_lista[6])
        e_n_guiaAcolhimento.insert(0, tree_lista[7])
        e_situacaoJuridica.insert(0, tree_lista[9])
        e_municipio.insert(0, tree_lista[10])
        e_n_processo.insert(0, tree_lista[8])
        e_motivoAcolhimento.insert(0, tree_lista[11])
        e_escola.insert(0, tree_lista[13])
        e_ano.insert(0, tree_lista[12])
        e_cursoProf.insert(0, tree_lista[14])

        
        def update():
            nome = e_name.get()
            data_nascimento = e_nasc.get()
            cor_raca = e_corRaca.get()
            data_acolhimento = e_dataAcolhimento.get()
            PIA = e_pia.get()
            n_guiaAcolhimento = e_n_guiaAcolhimento.get()
            situacao_juridica = e_situacaoJuridica.get()
            municipio = e_municipio.get()
            n_processo = e_n_processo.get()
            motivo_acolhimento = e_motivoAcolhimento.get()
            escola = e_escola.get()
            ano = e_ano.get()
            curso_prof = e_cursoProf.get()
            idade = calcular_idade(e_nasc)
            


            lista = [nome, data_nascimento, idade, cor_raca, data_acolhimento, PIA, n_guiaAcolhimento, n_processo, situacao_juridica, municipio, motivo_acolhimento, ano, escola, curso_prof, id_interno, ]

            if nome == '' or n_guiaAcolhimento == '' or n_processo == '':
                messagebox.showerror('Erro.','* indica um campo obrigatorio \n Existe(m) campo(s) obrigatorio(s) em vazio!')
            else:
                atualizar_infos(lista)
                messagebox.showinfo('Dado(s) atualizado(s) com sucesso!')

                e_name.delete(0,'end')
                e_nasc.delete(0,'end')
                e_corRaca.delete(0,'end')
                e_dataAcolhimento.delete(0,'end')
                e_pia.delete(0,'end')
                e_n_guiaAcolhimento.delete(0,'end')
                e_situacaoJuridica.delete(0,'end')
                e_municipio.delete(0,'end')
                e_n_processo.delete(0,'end')
                e_motivoAcolhimento.delete(0,'end')
                e_escola.delete(0,'end')
                e_ano.delete(0,'end')
                e_cursoProf.delete(0,'end')

            for widget in frame_direita.winfo_children():
                widget.destroy()

            display()

        b_confirmar = Button(frame_baixo, command=update, text="Confirmar", anchor=NW, font=('Ivy 13 bold'), bg='orange', fg='black', relief='raised', overrelief='ridge')
        b_confirmar.place(x=150,y=500)


    except IndexError:
        messagebox.showerror('Erro.','Seleciona um dos dados na')

def apagar():
    try:
        treev_dados = linha_1.focus()
        treev_dicionario = linha_1.item(treev_dados)
        tree_lista = treev_dicionario['values']

        id_interno = [tree_lista[0]]

        def excluir():
            deletar_infos(id_interno)
            messagebox.showinfo('Dado(s) deletado(s) da tabela com sucesso!') 

            for widget in frame_direita.winfo_children():
                widget.destroy()      

            display()

    
        b_confirmar = Button(frame_baixo, command=excluir, text="Confirmar", anchor=NW, font=('Ivy 13 bold'), bg='red', fg='black', relief='raised', overrelief='ridge')
        b_confirmar.place(x=150,y=500)

    except IndexError:
        messagebox.showerror('Erro.','Selecione a linha na tabela')

# funcao exportar
def exportar():
    exportar_infos()
    messagebox.showinfo('Dado(s) exportado(s) com sucesso!''\nFoi criado um arquivo excel em sua pasta de downloads!')

#nome frame meio
nome_meio = Label(frame_meio, text="Situação Educacional",  anchor=NW, font=('Ivy 13 bold'), bg=co2, fg=co1, relief='flat')
nome_meio.place(x=10, y=20)

#confg Nome
l_name = Label(frame_baixo, text='Nome*', anchor=NW, font=('Ivy 13 bold'), bg='#dbead5', relief='flat')
l_name.place(x=9, y=9)
e_name = Entry(frame_baixo, width=53, justify='left', relief='flat', highlightthickness=.5, highlightbackground="black")
e_name.place(x=65, y=9)

#config data de nascimento
l_nasc = Label(frame_baixo, text='Nascimento', anchor=NW, font=('Ivy 13 bold'), bg='#dbead5', relief='flat')
l_nasc.place(x=9, y=41)
e_nasc = DateEntry(frame_baixo, background='#225f3a', width=13, borderwidth=2, date_pattern="dd/mm/yyyy")
e_nasc.place(x=13, y=61)

#connfig caixa de opcoes para cor e raca
l_corRaca = Label(frame_baixo, text='Cor/Raça', anchor=NW, font=('Ivy 13 bold'), bg='#dbead5', relief='flat')
l_corRaca.place(x=126, y=41)
e_corRaca = ttk.Combobox(frame_baixo, values=list_corRaca, width=13)
e_corRaca.place(x=130, y=61)

#config data de acolhimento 
l_dataAcolhimento = Label(frame_baixo, text='Acolhimento', anchor=NW, font=('Ivy 13 bold'), bg='#dbead5', relief='flat')
l_dataAcolhimento.place(x=246, y=41)
e_dataAcolhimento = DateEntry(frame_baixo, background='#225f3a', width=19, borderwidth=2, date_pattern="dd/mm/yyyy")
e_dataAcolhimento.place(x=250, y=61)

#config PIA
l_pia = Label(frame_baixo, text='PIA', anchor=NW, font=('Ivy 13 bold'), bg='#dbead5', relief='flat')
l_pia.place(x=217, y=92)
e_pia = ttk.Combobox(frame_baixo, values=list_pia, width=24)
e_pia.place(x=222, y=113)

#config guia de acolhimento
l_n_guiaAcolhimento= Label(frame_baixo, text="N° Guia de Acolhimento*", anchor=NW, font=('Ivy 13 bold'), bg='#dbead5', relief='flat')
l_n_guiaAcolhimento.place(x=9,y=92)
e_n_guiaAcolhimento = Entry(frame_baixo,  width=31, justify='left', relief='flat', highlightthickness=.5, highlightbackground="black")
e_n_guiaAcolhimento.place(x=12,y=113)

#config situacao juridica
l_situacaoJuridica= Label(frame_baixo, text="Situacao Juridica", anchor=NW, font=('Ivy 13 bold'), bg='#dbead5', relief='flat')
l_situacaoJuridica.place(x=9,y=140)
e_situacaoJuridica = ttk.Combobox(frame_baixo, values=list_situacaoJuridica, width=59,)
e_situacaoJuridica.place(x=12,y=159)

#municipio
l_municipio= Label(frame_baixo, text="Municipio", anchor=NW, font=('Ivy 13 bold'), bg='#dbead5', relief='flat')
l_municipio.place(x=9,y=183)
e_municipio = Entry(frame_baixo, width=25, justify='left', relief='flat', highlightthickness=.5, highlightbackground="black")
e_municipio.place(x=12,y=203)

# config n_processo
l_n_processo= Label(frame_baixo, text="Numero do Processo*", anchor=NW, font=('Ivy 13 bold'), bg='#dbead5', relief='flat')
l_n_processo.place(x=200,y=183)
e_n_processo = Entry(frame_baixo, width=30, justify='left', relief='flat', highlightthickness=.5, highlightbackground="black")
e_n_processo.place(x=204,y=203)

#motivoAcolhimento
l_motivoAcolhimento= Label(frame_baixo, text="Motivo Do Acolhimento", anchor=NW, font=('Ivy 13 bold'), bg='#dbead5', relief='flat')
l_motivoAcolhimento.place(x=9,y=230)
e_motivoAcolhimento = ttk.Combobox(frame_baixo, width=59, values=list_motivoAcolhimento)
e_motivoAcolhimento.place(x=12,y=250)

#config escola
l_escola= Label(frame_baixo, text="Escola", anchor=NW, font=('Ivy 13 bold'), bg='#dbead5', relief='flat')
l_escola.place(x=9,y=340)
e_escola = Entry(frame_baixo, width=52, justify='left', relief='flat', highlightthickness=.5, highlightbackground="black")
e_escola.place(x=70,y=340)

# config ano
l_ano = Label(frame_baixo, text="Ano", anchor=NW, font=('Ivy 13 bold'), bg='#dbead5', relief='flat')
l_ano.place(x=9,y=370)
e_ano = Entry(frame_baixo, width=20, justify='left', relief='flat', highlightthickness=.5, highlightbackground="black")
e_ano.place(x=50,y=370)

#config crsoProf
l_cursoProf = Label(frame_baixo, text="Faz Curso Profissionalizante?", anchor=NW, font=('Ivy 13 bold'), bg='#dbead5', relief='flat')
l_cursoProf.place(x=9,y=400)
e_cursoProf = ttk.Combobox(frame_baixo, values=list_sn, width=10)
e_cursoProf.place(x=250,y=400)

# Botoes
b_cadastrar = Button(frame_baixo, command=inserir, text="Cadastrar", anchor=NW, font=('Ivy 12 bold'), bg=co2, fg=co1, relief='raised', overrelief='ridge')
b_cadastrar.place(x=9,y=455)

b_export = Button(frame_baixo, command=exportar, text="Exportar", anchor=NW, font=('Ivy 12 bold'), bg='#5187DD', fg=co1, relief='raised', overrelief='ridge')
b_export.place(x=120,y=455)

b_atualizar = Button(frame_baixo, command=atualizar, text="Alterar", anchor=NW, font=('Ivy 12 bold'), bg='#ECAB0F', fg=co1, relief='raised', overrelief='ridge')
b_atualizar.place(x=230,y=455)

b_deletar = Button(frame_baixo, command=apagar, text="Apagar", anchor=NW, font=('Ivy 12 bold'), bg='#DC474D', fg=co1, relief='raised', overrelief='ridge')
b_deletar.place(x=320,y=455)

# funcao para exibir
def display():

# variavel global        
    global linha_1

    lista = mostrar_infos()

    #valores titulos de colunas
    cabecalho = ['Nº','Nome','Data de Nascimento','Idade','Cor/Raça','Data do Acolhimento','PIA', 'Numero da Guia de Acolhimento', 'Numero do Processo','Situação Juridica', 'Municipio','Motivo do Acolhimento','Escola','Ano', 'Faz Curso Profissionalizante']

#   define a primeira linha da tabela
    linha_1 = ttk.Treeview(frame_direita, selectmode='extended', columns=cabecalho, show='headings')

#   cria barra de rolagem
    ver=ttk.Scrollbar(frame_direita, orient='vertical', command=linha_1.yview)
    hor=ttk.Scrollbar(frame_direita, orient='horizontal', command=linha_1.xview)

#   configura o tamanho e posicao em tela
    linha_1.place(x=1, y=1, width=670, height=670)
    ver.place(x=665, y=1, width=15, height=590)
    hor.place(x=1, y=585, width=670, height=15)
    frame_direita.grid_rowconfigure(0, weight=1)

#   cofigura tamanho da barra dentro do scrollbar
    linha_1.configure(yscrollcommand=ver.set, xscrollcommand=hor.set)


#   alinhamento de colunas
    hd=["nw","nw","nw","nw","nw","nw","nw","nw","nw","nw","nw","nw","nw","nw","nw","nw"]
    h=[30,170,100,40,80,100,170,100,100,140,90,150,100,70,100,100]
    n=0

    for col in cabecalho:
        linha_1.heading(col, text=col.title(), anchor=CENTER)
        linha_1.column(col, width=h[n], anchor=hd[n])

        n+=1

    for item in lista:
        linha_1.insert('', 'end', values=item)



#chamando a funcao 
display()

janela.mainloop()
