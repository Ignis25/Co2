import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns

donnees2013 = pd.read_csv('2013_data.csv', sep = ';', encoding = 'latin-1')

st.title("Projet Co2")
st.write("Projet réalisé par François Vergne, Drazen Saric & Arnaud Colombel")
st.sidebar.title("Sommaire")
pages=["Présentation du Projet", "Data Visualisation", "Machine Learning", "Résultats"]
page=st.sidebar.radio("Aller vers", pages)
if st.checkbox("Afficher"):
  st.write("Suite du Streamlit")

if page == page[1]:
  st.write("### Data Visualisation")
