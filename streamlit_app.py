import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import chardet
import matplotlib.pyplot as plt

st.title("Projet Co2")
st.write("Projet réalisé par François Vergne, Drazen Saric & Arnaud Colombel")

# Permettre à l'utilisateur de télécharger un fichier CSV
uploaded_file = st.file_uploader("Choisissez un fichier CSV", type="csv")

if uploaded_file is not None:
    try:
        # Lire le fichier brut pour détecter l'encodage
        raw_data = uploaded_file.getvalue()
        result = chardet.detect(raw_data)
        encoding = result['encoding']
        
        # Lire le fichier CSV avec l'encodage détecté
        df = pd.read_csv(uploaded_file, sep=';', encoding=encoding, on_bad_lines='skip', low_memory=False)
        
        # Afficher les premières lignes du fichier CSV
        st.write("Premières lignes du fichier CSV :")
        
    except pd.errors.ParserError as e:
        st.error(f"Erreur lors de la lecture du fichier CSV : {e}")
        st.stop()
    except Exception as e:
        st.error(f"Une erreur est survenue : {e}")
        st.stop()
else:
    st.write("Veuillez télécharger un fichier CSV pour continuer.")

    

st.sidebar.title("Sommaire")
pages=["Présentation du Projet", "Data Visualisation", "Machine Learning", "Résultats"]
page=st.sidebar.radio("Aller vers", pages)

if page == pages[0]:
  # Afficher les données
    st.write("Voici les données du fichier CSV :")
    st.write(df.head())
     # Afficher quelques statistiques sur les données
    st.write("Résumé statistique :")
    st.write(df.describe())

    if page == pages[1]:
        st.write("### Data Visualisation")
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.violinplot(x='Carburant', y='CO2 (g/km)', data=df, palette='Set2', ax=ax)
        ax.set_title("Distribution du CO2 par type de carburant")
        st.pyplot(fig)



