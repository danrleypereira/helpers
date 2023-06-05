import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from pdb import set_trace


colunas_respostas = ['Idade ', 'SEXO', 'CURSO', 'SEMESTRE']
# faixas: até 20, entre 20 e 25; 25 e 30; 30 e 40
labels = ['F1', 'F2', 'F3', 'F4', 'F5']
width = 0.35
fig, ax = plt.subplots()

df = pd.read_csv(r'src/respostas.csv')
df_higienizado = df.get(coluna for coluna in colunas_respostas)
df_higienizado['SEMESTRE'].unique()
idades = pd.value_counts(df_higienizado['Idade '])
semestres = pd.value_counts(df_higienizado['SEMESTRE'])
cursos = pd.value_counts(df_higienizado['CURSO'])
sexos = pd.value_counts(df_higienizado['SEXO'])
set_trace()
df_higienizado['SEXO'].unique()
df_higienizado['CURSO'].unique()

# print graphical


print(df)
