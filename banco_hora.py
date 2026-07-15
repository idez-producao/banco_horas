import pandas as pd
import streamlit as st
import plotly.express as px
from datetime import datetime


df = pd.read_csv('banco_horas.csv', sep=",")
df_atual = pd.read_csv('banco_hora_2026.csv', sep=",")

#funcao para criar uma senha variavel de acordo com o dia
def senha_global():
    data = datetime.now().strftime("%d%m")
    return data

#funcao que cria o grafico a partir do nome - grafico por ano
nome = "joao" #essa variavel é a que irar mudar 
def grafico_ano(df,nome):
    #essas entredas nessa funcao é os Dados e o nome a ser selecionado
    df_nome = df[df['nome']== nome].copy() #selecioando o apenas os dados referente ao nome
    a = df_nome[['2022','2023','2024','2025','2026']].sum(axis=1).values[0] #somatorio de todos os anos em minutos
    #transformando os valores que estao em minutos para horas:min
    a_hora = a//60
    a_min = a%60

    # Defina o 'Nome' como índice ANTES de transpor
    df_grafico = df_nome.set_index('nome').T.reset_index()
    #transformando a coluna index em numero
    df_grafico['index'] = pd.to_numeric(df_grafico['index'], errors='coerce')

    # Vamos garantir que os nomes fiquem na ordem que aparecem no DF
    df_grafico = df_grafico.sort_values(by='index', ascending=True)

    # Criar coluna 'Status' usando uma função lambda
    df_grafico['status'] = df_grafico[nome].apply(lambda x: 'Positivo' if x >= 0 else 'Negativo')
    
    # Criando o gráfico de barras
    fig = px.bar(
        df_grafico,
        x= 'index',
        y= nome,
        color = 'status',
        title= f'TOTAL = {a} minutos || {a_hora} horas e {a_min} minutos',
        text_auto= nome, # Adiciona o valor em cima das barras de forma resumida
        # MAPEAMENTO MANUAL DE CORES (O segredo!)
        color_discrete_map={
            'Positivo': '#7FFFD4', # Verde Esmeralda (Hexadecimal)
            'Negativo': '#FF6347'  # Vermelho Alizarin
        }
    )
    # Adicionar uma linha de referência no valor 0
    fig.add_hline(y=0, line_dash="dash", line_color="black")

    # 💡 Mudando os nomes dos eixos após a criação do gráfico:
    fig.update_xaxes(title_text='Ano')
    #fig.update_yaxes(title_text='minuto')

    #mudando as cores das grades atraz do grafico
    fig.update_yaxes(showgrid=False, gridcolor='LightGray')
    fig.update_xaxes(showgrid=True, gridcolor='#333333',gridwidth=1)

    # 💡 A MÁGICA PARA MUDAR O FUNDO:
    fig.update_layout(
        # 1. Muda a cor da área interna do gráfico (Ex: Um cinza bem clarinho)
        plot_bgcolor='#04458F',

        # 2. Muda a cor de toda a área externa (Ex: Branco puro)
        paper_bgcolor="#04458F"
    )
    return fig
    #fig.show()    
    

#funcao que cria o grafico a partir do nome - grafico por mes ano atual
def grafico_mes(df,nome):
    df_nome_atual = df_atual[df_atual['nome']== nome].copy()
    
    #somando os valores na linha do nome selecionado
    b = df_nome_atual[['1','2','3','4','5','6']].sum(axis=1).values[0]
    #transformando os minutos em horas e minutos
    b_hora = b//60
    b_min = b%60

    # Defina o 'Nome' como índice ANTES de transpor
    df_grafico_atual = df_nome_atual.set_index('nome').T.reset_index()
    #transformando a coluna index em numero
    df_grafico_atual['index'] = pd.to_numeric(df_grafico_atual['index'], errors='coerce')

    # Vamos garantir que os nomes fiquem na ordem que aparecem no DF
    df_grafico_atual = df_grafico_atual.sort_values(by='index', ascending=True)

    # Criar coluna 'Status' usando uma função lambda
    df_grafico_atual['status'] = df_grafico_atual[nome].apply(lambda x: 'Positivo' if x >= 0 else 'Negativo')

    # Criando o gráfico de barras
    fig = px.bar(
        df_grafico_atual,
        x= 'index',
        y= nome,
        color = 'status',
        title= f'TOTAL 2026 = {b} minutos || {b_hora} horas e {b_min} minutos',
        text_auto= nome, # Adiciona o valor em cima das barras de forma resumida
        # MAPEAMENTO MANUAL DE CORES (O segredo!)
        color_discrete_map={
            'Positivo': '#7FFFD4', # Verde Esmeralda (Hexadecimal)
            'Negativo': '#FF6347'  # Vermelho Alizarin
        }
    )
    # Adicionar uma linha de referência no valor 0
    fig.add_hline(y=0, line_dash="dash", line_color="black")

    # 💡 Mudando os nomes dos eixos após a criação do gráfico:
    fig.update_xaxes(title_text='Meses')
    #fig.update_yaxes(title_text='minuto')

    #mudando as cores das grades atraz do grafico
    fig.update_yaxes(showgrid=False, gridcolor="#ECE2E2")
    fig.update_xaxes(showgrid=True, gridcolor='#333333',gridwidth=1)

    # 💡 A MÁGICA PARA MUDAR O FUNDO:
    fig.update_layout(
        # 1. Muda a cor da área interna do gráfico (Ex: Um cinza bem clarinho)
        plot_bgcolor="#04458F",

        # 2. Muda a cor de toda a área externa (Ex: Branco puro)
        paper_bgcolor="#04458F"
    )

    #fig.show()
    return fig


############################################################################
############################################################################
#inicio da pagina de navegacao
st.markdown("#### Banco de Horas")

#barra lateal
barra = st.sidebar

with barra:
    funcionario = st.radio("Nome:", ["","adriano","elionay","fernando","inacio","joao","manuel","rodrigo","samuel","thiago","toin"])

if funcionario == "":
    st.write("Selecione seu nome na barra lateal.")

elif funcionario == "adriano":
    st.write("A senha é o dia e o mês do seu aniversario!")
    senha = st.text_input("Sua Senha: ")

    if senha == senha_global() or senha == "0107":
        st.plotly_chart(grafico_ano(df,funcionario),)
        st.plotly_chart(grafico_mes(df_atual,funcionario))
        
    else:
        st.write("Tente Novamente!")
    
elif funcionario == "elionay":
    st.write("A senha é o dia e o mês do seu aniversario!")
    senha = st.text_input("Sua Senha: ")

    if senha == senha_global() or senha == "1234":
        st.plotly_chart(grafico_ano(df,funcionario),)
        st.plotly_chart(grafico_mes(df_atual,funcionario))
        
    else:
        st.write("Tente Novamente!")

elif funcionario == "fernando":
    st.write("A senha é o dia e o mês do seu aniversario!")
    senha = st.text_input("Sua Senha: ")

    if senha == senha_global() or senha == "2602":
        st.plotly_chart(grafico_ano(df,funcionario),)
        st.plotly_chart(grafico_mes(df_atual,funcionario))
        
    else:
        st.write("Tente Novamente!")

elif funcionario == "inacio":
    st.write("A senha é o dia e o mês do seu aniversario!")
    senha = st.text_input("Sua Senha: ")

    if senha == senha_global() or senha == "1234":
        st.plotly_chart(grafico_ano(df,funcionario),)
        st.plotly_chart(grafico_mes(df_atual,funcionario))
        
    else:
        st.write("Tente Novamente!")

elif funcionario == "joao":
    st.write("A senha é o dia e o mês do seu aniversario!")
    senha = st.text_input("Sua Senha: ")

    if senha == senha_global() or senha == "0407":
        st.plotly_chart(grafico_ano(df,funcionario),)
        st.plotly_chart(grafico_mes(df_atual,funcionario))
        
    else:
        st.write("Tente Novamente!")

elif funcionario == "manuel":
    st.write("A senha é o dia e o mês do seu aniversario!")
    senha = st.text_input("Sua Senha: ")

    if senha == senha_global() or senha == "1234":
        st.plotly_chart(grafico_ano(df,funcionario),)
        st.plotly_chart(grafico_mes(df_atual,funcionario))
        
    else:
        st.write("Tente Novamente!")

elif funcionario == "rodrigo":
    st.write("A senha é o dia e o mês do seu aniversario!")
    senha = st.text_input("Sua Senha: ")

    if senha == senha_global() or senha == "1902":
        st.plotly_chart(grafico_ano(df,funcionario),)
        st.plotly_chart(grafico_mes(df_atual,funcionario))
        
    else:
        st.write("Tente Novamente!")

elif funcionario == "samuel":
    st.write("A senha é o dia e o mês do seu aniversario!")
    senha = st.text_input("Sua Senha: ")

    if senha == senha_global() or senha == "1306":
        st.plotly_chart(grafico_ano(df,funcionario),)
        st.plotly_chart(grafico_mes(df_atual,funcionario))
        
    else:
        st.write("Tente Novamente!")

elif funcionario == "thiago":
    st.write("A senha é o dia e o mês do seu aniversario!")
    senha = st.text_input("Sua Senha: ")

    if senha == senha_global() or senha == "2105":
        st.plotly_chart(grafico_ano(df,funcionario),)
        st.plotly_chart(grafico_mes(df_atual,funcionario))
        
    else:
        st.write("Tente Novamente!")

elif funcionario == "toin":
    st.write("A senha é o dia e o mês do seu aniversario!")
    senha = st.text_input("Sua Senha: ")

    if senha == senha_global() or senha == "0809":
        st.plotly_chart(grafico_ano(df,funcionario),)
        st.plotly_chart(grafico_mes(df_atual,funcionario))
        
    else:
        st.write("Tente Novamente!")

