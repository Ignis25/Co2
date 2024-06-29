import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import chardet
import matplotlib.pyplot as plt

st.title('Lire un fichier CSV')

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

if 'Carburant' in df.columns and 'CO2 (g/km)' in df.columns:
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.violinplot(x='Carburant', y='CO2 (g/km)', data=df, palette='Set2', ax=ax)
    ax.set_title("Distribution du CO2 par type de carburant")
    st.pyplot(fig)
else:
    st.error("Les colonnes 'carburant' ou 'co2 (g/km)' ne sont pas présentes dans le DataFrame.")


