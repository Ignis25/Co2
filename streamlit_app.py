import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns

import webbrowser
webbrowser.open('http://streamlit.io')

donnees2013 = pd.read_csv('/content/drive/MyDrive/Projet_Co2/2013_data.csv', sep = ';', encoding = 'latin-1')
st.title("Projet Co2")
st.write("Projet réalisé par François Vergne, Drazen Saric & Arnaud Colombel")
st.sidebar.title("Sommaire")
pages=["Présentation du Projet", "Data Visualisation", "Machine Learning", "Résultats"]
page=st.sidebar.radio("Aller vers", pages)
if st.checkbox("Afficher"):
  st.write("Suite du Streamlit")

if page == page[1]:
  st.write("### Data Visualisation")

fig = sns.violinplot(x='CARBURANT', y='CO2 (G/KM)', data=donnees2013, palette='Set2')
plt.title("Distribution de l'âge des passagers")
plt.title('Distribution des émissions de CO2 par type de carburant')
plt.xlabel('Type de carburant')
plt.ylabel('Émissions de CO2 (g/km)')
plt.xticks(rotation=45)
st.pyplot(fig)

plt.figure(figsize=(10, 6))

