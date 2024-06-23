import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns

import webbrowser
webbrowser.open('http://streamlit.io')
url = 'https://github.com/Ignis25/Co2/blob/b43b8a994daaaadd910854d51f7ba9ef7688bc24/2013_data.csv'
donnees2013 = pd.read_csv(url, sep=';', encoding='utf-8', error_bad_lines=False, low_memory=False)
except pd.errors.ParserError as e:
    st.error(f"Erreur lors de la lecture du fichier CSV : {e}")
    st.stop()


st.title("Projet Co2")
st.write("Projet réalisé par François Vergne, Drazen Saric & Arnaud Colombel")
st.sidebar.title("Sommaire")
pages=["Présentation du Projet", "Data Visualisation", "Machine Learning", "Résultats"]
page=st.sidebar.radio("Aller vers", pages)
if st.checkbox("Afficher"):
  st.write("Suite du Streamlit")
  
if page == page[0]:
  st.dataframe(donnees2013.head(10))

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

