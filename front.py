from tkinter import Label
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import back
from bokeh.plotting import figure, show

#back.conectar_mysql()

st.title('SIPERJ')
st.write("Bem-vindo ao SIPERJ - Sistema de Planejamento Estratégico da cidade do Rio de Janeiro.")

def bairros_ap():
    st.header("Bairros e suas respectivas áreas de planejamento:")
    lista = back.areas_de_planejamento()
    bairro = []
    ap = []
    for i in lista:
        bairro.append(i[0])
        ap.append(i[1])

    dict = { 'Bairro':bairro, 'Área de Planejamento':ap}

    df = pd.DataFrame(
        dict
    )

    st.table(df)

def atividades_bairro(nome_bairro):
    st.header("Quantidade de Empregados por atividade Econômica em "+nome_bairro)
    lista = back.atividade_economica()
    atividade = []
    quantidade = []
    for i in lista:
        atividade.append(i[0])
        quantidade.append(i[1])

    dict = { 'Atividade Econômica': atividade, 'Número de Empregados':quantidade}
    df = pd.DataFrame(dict)
    st.table(df)

def IDS_medio_RA():
    st.header("Índice de Desenvolvimento Social Médio por Região Administrativa")
    lista = back.IDS_medio_RA()
    ra = []
    ids = []
    for i in lista:
        ra.append(i[0])
        ids.append(i[1])

    dict = {'Região Administrativa': ra, 'IDS médio': ids}
    df = pd.DataFrame(dict)
    st.table(df)

def pobreza_AP():
    st.header("Total de Famílias em Extrema Pobreza por Área de Planejamento")
    lista = back.pobreza_AP()
    familias = []
    ap = []
    for i in lista:
        ap.append(i[1])
        familias.append(i[2])

    dict = {'Área de Planejamento':ap, 'Número de Famílias':familias}
    df = pd.DataFrame(dict)
    st.table(df)

num_bairro = 5
def atividades_zero_bairro(num_bairro):
    st.header("Atividades Econômicas sem empregados no bairro "+back.getNomeBairro(num_bairro))
    lista = []
    for i in back.atividades_zero(num_bairro):
        lista.append(i[0])
    dict = {'Atividades Econômicas': lista}
    df = pd.DataFrame(dict)
    st.table(df)


bairros_ap()
atividades_bairro("Bangu")
IDS_medio_RA()
pobreza_AP()
atividades_zero_bairro(num_bairro)

