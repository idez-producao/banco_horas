import pandas as pd
import streamlit as st
from datetime import datetime

df_ano = pd.read_csv("banco_horas.csv", sep=",")
df_mes = pd.read_csv("banco_hora_2026.csv", sep=",")

#st.write(df_ano)

#st.write(df_mes)


#funcao para criar uma senha variavel de acordo com o dia
def senha_global():
    data = datetime.now().strftime("%d%m")
    return data

###########funcao que pega o ano e o nome#################
def ano_nome(funcionario,df_ano):
    df = df_ano
    df_ = df[["ano",funcionario]].copy()
    lista_ano = df_['ano'].to_list()
    lista_valor = df_[funcionario].to_list()

    return lista_ano, lista_valor


###########funcao que pega o mes e o nome#################
def ano_atual(funcionario,df_mes):
    df = df_mes
    df_ = df[["mes",funcionario]].copy()
    lista_ano = df_['mes'].to_list()
    lista_valor = df_[funcionario].to_list()

    return lista_ano, lista_valor



########## craiando a estrutura da visualizacao ##########################
#inicio da pagina de navegacao
#st.set_page_config(layout="wide")
st.markdown("#### Banco de Horas")

#barra lateal
barra = st.sidebar

with barra:
    funcionario_ = st.radio("Nome:", ["","adriano","elionay","fernando","inacio","joao","manoel","rodrigo","samuel","thiago","toin"])

if funcionario_ == "":
    st.write("Selecione seu nome na barra lateal.")

elif funcionario_ == "adriano":
    st.write("A senha é o dia e o mês do seu aniversario!")
    senha = st.text_input("Sua Senha: ")

    if senha == senha_global() or senha == "0107":
        ano = ano_nome(funcionario_, df_ano)
        mes = ano_atual(funcionario_, df_mes)

        total = sum(ano[1])

        st.markdown(f"### BANCO DE HORAS POR ANO | TOTAL= {total} min")

        for i in range(len(ano[0])):
            st.markdown(f"### {ano[0][i]} : {ano[1][i]} min")
        
        st.write("")
        st.write("")
        st.write("########################################################################################")
        
        total_mes = sum(mes[1])
        st.markdown(f"### BANCO DE HORAS DO ANO 2026 | TOTAL= {total_mes} min")
        for i in range(len(mes[0])):
            st.markdown(f"### MÊS - {mes[0][i]} : {mes[1][i]} min")
        st.write("########################################################################################")
        
    else:
        st.write("Tente Novamente!")


elif funcionario_ == "elionay":
    st.write("A senha é o dia e o mês do seu aniversario!")
    senha = st.text_input("Sua Senha: ")

    if senha == senha_global() or senha == "1234":
        ano = ano_nome(funcionario_, df_ano)
        mes = ano_atual(funcionario_, df_mes)

        total = sum(ano[1])

        st.markdown(f"### BANCO DE HORAS POR ANO | TOTAL= {total} min")

        for i in range(len(ano[0])):
            st.markdown(f"### {ano[0][i]} : {ano[1][i]} min")
        
        st.write("")
        st.write("")
        st.write("########################################################################################")
        
        total_mes = sum(mes[1])
        st.markdown(f"### BANCO DE HORAS DO ANO 2026 | TOTAL= {total_mes} min")
        for i in range(len(mes[0])):
            st.markdown(f"### MÊS - {mes[0][i]} : {mes[1][i]} min")
        st.write("########################################################################################")
        
    else:
        st.write("Tente Novamente!")

elif funcionario_ == "fernando":
    st.write("A senha é o dia e o mês do seu aniversario!")
    senha = st.text_input("Sua Senha: ")

    if senha == senha_global() or senha == "2602":
        ano = ano_nome(funcionario_, df_ano)
        mes = ano_atual(funcionario_, df_mes)

        total = sum(ano[1])

        st.markdown(f"### BANCO DE HORAS POR ANO | TOTAL= {total} min")

        for i in range(len(ano[0])):
            st.markdown(f"### {ano[0][i]} : {ano[1][i]} min")
        
        st.write("")
        st.write("")
        st.write("########################################################################################")
        
        total_mes = sum(mes[1])
        st.markdown(f"### BANCO DE HORAS DO ANO 2026 | TOTAL= {total_mes} min")
        for i in range(len(mes[0])):
            st.markdown(f"### MÊS - {mes[0][i]} : {mes[1][i]} min")
        st.write("########################################################################################")
        
    else:
        st.write("Tente Novamente!")

elif funcionario_ == "inacio":
    st.write("A senha é o dia e o mês do seu aniversario!")
    senha = st.text_input("Sua Senha: ")

    if senha == senha_global() or senha == "3009":
        ano = ano_nome(funcionario_, df_ano)
        mes = ano_atual(funcionario_, df_mes)

        total = sum(ano[1])

        st.markdown(f"### BANCO DE HORAS POR ANO | TOTAL= {total} min")

        for i in range(len(ano[0])):
            st.markdown(f"### {ano[0][i]} : {ano[1][i]} min")
        
        st.write("")
        st.write("")
        st.write("########################################################################################")
        
        total_mes = sum(mes[1])
        st.markdown(f"### BANCO DE HORAS DO ANO 2026 | TOTAL= {total_mes} min")
        for i in range(len(mes[0])):
            st.markdown(f"### MÊS - {mes[0][i]} : {mes[1][i]} min")
        st.write("########################################################################################")
        
    else:
        st.write("Tente Novamente!")

elif funcionario_ == "joao":
    st.write("A senha é o dia e o mês do seu aniversario!")
    senha = st.text_input("Sua Senha: ")

    if senha == senha_global() or senha == "0407":
        ano = ano_nome(funcionario_, df_ano)
        mes = ano_atual(funcionario_, df_mes)

        total = sum(ano[1])

        st.markdown(f"### BANCO DE HORAS POR ANO | TOTAL= {total} min")

        for i in range(len(ano[0])):
            st.markdown(f"### {ano[0][i]} : {ano[1][i]} min")
        
        st.write("")
        st.write("")
        st.write("########################################################################################")
        
        total_mes = sum(mes[1])
        st.markdown(f"### BANCO DE HORAS DO ANO 2026 | TOTAL= {total_mes} min")
        for i in range(len(mes[0])):
            st.markdown(f"### MÊS - {mes[0][i]} : {mes[1][i]} min")
        st.write("########################################################################################")
        
    else:
        st.write("Tente Novamente!")
    
elif funcionario_ == "manoel":
    st.write("A senha é o dia e o mês do seu aniversario!")
    senha = st.text_input("Sua Senha: ")

    if senha == senha_global() or senha == "3105":
        ano = ano_nome(funcionario_, df_ano)
        mes = ano_atual(funcionario_, df_mes)

        total = sum(ano[1])

        st.markdown(f"### BANCO DE HORAS POR ANO | TOTAL= {total} min")

        for i in range(len(ano[0])):
            st.markdown(f"### {ano[0][i]} : {ano[1][i]} min")
        
        st.write("")
        st.write("")
        st.write("########################################################################################")
        
        total_mes = sum(mes[1])
        st.markdown(f"### BANCO DE HORAS DO ANO 2026 | TOTAL= {total_mes} min")
        for i in range(len(mes[0])):
            st.markdown(f"### MÊS - {mes[0][i]} : {mes[1][i]} min")
        st.write("########################################################################################")
        
    else:
        st.write("Tente Novamente!")
    
elif funcionario_ == "rodrigo":
    st.write("A senha é o dia e o mês do seu aniversario!")
    senha = st.text_input("Sua Senha: ")

    if senha == senha_global() or senha == "1902":
        ano = ano_nome(funcionario_, df_ano)
        mes = ano_atual(funcionario_, df_mes)

        total = sum(ano[1])

        st.markdown(f"### BANCO DE HORAS POR ANO | TOTAL= {total} min")

        for i in range(len(ano[0])):
            st.markdown(f"### {ano[0][i]} : {ano[1][i]} min")
        
        st.write("")
        st.write("")
        st.write("########################################################################################")
        
        total_mes = sum(mes[1])
        st.markdown(f"### BANCO DE HORAS DO ANO 2026 | TOTAL= {total_mes} min")
        for i in range(len(mes[0])):
            st.markdown(f"### MÊS - {mes[0][i]} : {mes[1][i]} min")
        st.write("########################################################################################")
        
    else:
        st.write("Tente Novamente!")

elif funcionario_ == "samuel":
    st.write("A senha é o dia e o mês do seu aniversario!")
    senha = st.text_input("Sua Senha: ")

    if senha == senha_global() or senha == "1306":
        ano = ano_nome(funcionario_, df_ano)
        mes = ano_atual(funcionario_, df_mes)

        total = sum(ano[1])

        st.markdown(f"### BANCO DE HORAS POR ANO | TOTAL= {total} min")

        for i in range(len(ano[0])):
            st.markdown(f"### {ano[0][i]} : {ano[1][i]} min")
        
        st.write("")
        st.write("")
        st.write("########################################################################################")
        
        total_mes = sum(mes[1])
        st.markdown(f"### BANCO DE HORAS DO ANO 2026 | TOTAL= {total_mes} min")
        for i in range(len(mes[0])):
            st.markdown(f"### MÊS - {mes[0][i]} : {mes[1][i]} min")
        st.write("########################################################################################")
        
    else:
        st.write("Tente Novamente!")

elif funcionario_ == "thiago":
    st.write("A senha é o dia e o mês do seu aniversario!")
    senha = st.text_input("Sua Senha: ")

    if senha == senha_global() or senha == "1234":
        ano = ano_nome(funcionario_, df_ano)
        mes = ano_atual(funcionario_, df_mes)

        total = sum(ano[1])

        st.markdown(f"### BANCO DE HORAS POR ANO | TOTAL= {total} min")

        for i in range(len(ano[0])):
            st.markdown(f"### {ano[0][i]} : {ano[1][i]} min")
        
        st.write("")
        st.write("")
        st.write("########################################################################################")
        
        total_mes = sum(mes[1])
        st.markdown(f"### BANCO DE HORAS DO ANO 2026 | TOTAL= {total_mes} min")
        for i in range(len(mes[0])):
            st.markdown(f"### MÊS - {mes[0][i]} : {mes[1][i]} min")
        st.write("########################################################################################")
        
    else:
        st.write("Tente Novamente!")

elif funcionario_ == "toin":
    st.write("A senha é o dia e o mês do seu aniversario!")
    senha = st.text_input("Sua Senha: ")

    if senha == senha_global() or senha == "0809":
        ano = ano_nome(funcionario_, df_ano)
        mes = ano_atual(funcionario_, df_mes)

        total = sum(ano[1])

        st.markdown(f"### BANCO DE HORAS POR ANO | TOTAL= {total} min")

        for i in range(len(ano[0])):
            st.markdown(f"### {ano[0][i]} : {ano[1][i]} min")
        
        st.write("")
        st.write("")
        st.write("########################################################################################")
        
        total_mes = sum(mes[1])
        st.markdown(f"### BANCO DE HORAS DO ANO 2026 | TOTAL= {total_mes} min")
        for i in range(len(mes[0])):
            st.markdown(f"### MÊS - {mes[0][i]} : {mes[1][i]} min")
        st.write("########################################################################################")
        
    else:
        st.write("Tente Novamente!")


#st.write(ano_nome("adriano",df_ano)[1])
#st.write(ano_atual("adriano",df_mes)[1])

#########isso foi apenas um espermento ##########################
#st.title("Desempenho de Vendas")

# O st.dataframe aceita formatação com barras visuais
#st.dataframe(
#    df_ano,
#    column_config={
#        "inacio": st.column_config.ProgressColumn(
#            "inacio",
#            format="%d",
#            min_value=0,
#            max_value=int(df_ano["inacio"].max()), # A maior barra será o maior valor de vendas
#        ),
#    },
#    hide_index=True,
#    use_container_width=True
#)
