import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import chardet

uploaded_file = st.file_uploader("Choisissez un fichier CSV", type="csv")

if uploaded_file is not None:
    try:
        # Lire le fichier brut pour détecter l'encodage
        raw_data = uploaded_file.getvalue()
        result = chardet.detect(raw_data)
        encoding = result['encoding']
        
        # Lire le fichier CSV avec l'encodage détecté
        df = pd.read_csv(uploaded_file, sep=';', encoding=encoding, on_bad_lines='skip', low_memory=False)
        
        # Afficher les données
        st.write("Voici les données du fichier CSV :")
        st.dataframe(df)
        
        # Afficher quelques statistiques sur les données
        st.write("Résumé statistique :")
        st.write(df.describe())
        
        # Afficher les premières lignes du fichier CSV
        st.write("Premières lignes du fichier CSV :")
        st.write(df.head())
    except pd.errors.ParserError as e:
        st.error(f"Erreur lors de la lecture du fichier CSV : {e}")
        st.stop()
    except Exception as e:
        st.error(f"Une erreur est survenue : {e}")
        st.stop()
else:
    st.write("Veuillez télécharger un fichier CSV pour continuer.")
    
st.title("Projet Co2")
st.write("Projet réalisé par François Vergne, Drazen Saric & Arnaud Colombel")
st.sidebar.title("Sommaire")
pages=["Présentation du Projet", "Data Visualisation", "Machine Learning", "Résultats"]
page=st.sidebar.radio("Aller vers", pages)
if st.checkbox("Afficher"):
  st.write("Suite du Streamlit")
  
if page == page[0]:
  st.dataframe(url.head(10))

if page == page[1]:
  st.write("### Data Visualisation")

fig = sns.violinplot(x='CARBURANT', y='CO2 (G/KM)', data=url, palette='Set2')
plt.title("Distribution de l'âge des passagers")
plt.title('Distribution des émissions de CO2 par type de carburant')
plt.xlabel('Type de carburant')
plt.ylabel('Émissions de CO2 (g/km)')
plt.xticks(rotation=45)
st.pyplot(fig)

plt.figure(figsize=(10, 6))

