import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import chardet
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.colors as mcolors
import sklearn
from sklearn.preprocessing import OrdinalEncoder
from sklearn.linear_model import LinearRegression
import io
import plotly.express as px
import plotly.graph_objects as go
import joblib
import pickle
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report           
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import xgboost as xgb
from sklearn.metrics import mean_squared_error, r2_score


# Permettre à l'utilisateur de télécharger un fichier CSV
uploaded_file = st.file_uploader("Choisissez un fichier CSV", type="csv")



if uploaded_file is not None:
    try:
        # Lire le fichier brut pour détecter l'encodage
        raw_data = uploaded_file.getvalue()
        result = chardet.detect(raw_data)
        encoding = result['encoding']
        
        # Lire le fichier CSV avec l'encodage détecté
        donnees2013 = pd.read_csv(uploaded_file, sep=';', encoding=encoding, on_bad_lines='skip', low_memory=False)
        
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


#Début du code pour tout le monde

st.title("Projet Co2")
st.image("https://cdn.futura-sciences.com/buildsv6/images/wide1920/7/b/2/7b2a2ed969_96670_voiture-propre.jpg", width=300)
st.title("Émissions de CO2 et Véhicules : À la Conquête d'un Futur Plus Vert")



#Sidebar 
st.sidebar.title("Sommaire")
pages=["Introduction","Contexte","Exploration des données", "DataVizualization", "Modélisation 1", "Modélisation 2"]
page=st.sidebar.radio("Naviguer vers", pages)
st.sidebar.write("\n")
st.sidebar.write("\n")
st.sidebar.write("\n")
st.sidebar.write("\n")
st.sidebar.image("https://www.lympho.fr/images/quisommesnous/qui-sommes-nous.jpg", width = 200)


 
# Qui sommes-nous ?
add_selectbox = st.sidebar.selectbox(
    "",
    ("","Arnaud Colombel", "Saric Drazen", "François vergne"))
if add_selectbox == "":
    st.sidebar.write("")
if add_selectbox == "Arnaud Colombel":
    st.sidebar.write("Travaillant en supply chain le transport est au coeur de mon métier. Il y a 2 ans via une politique RSE nous avons commencé à utiliser le transport ferroviaire de livraison de containers pour limiter nos émissions de Co2. ")
if add_selectbox == "Saric Drazen":
    st.sidebar.write("En tant que Responsable Réseau Drive en Distribution, je suis en charge de la gestion de quatre centres de distribution. Mon rôle inclut la supervision des opérations, l'optimisation des processus logistiques et le développement de solutions innovantes pour améliorer l'efficacité et la satisfaction client. Un des défis majeurs dans la livraison à domicile (LAD) est la gestion du dernier kilomètre, qui représente souvent le coût le plus élevé dans la chaîne logistique. Pour relever ce défi, je souhaite développer un projet visant à réduire les émissions de CO2 et à montrer à nos clients, via notre flotte électrique, notre engagement RSE.")   
if add_selectbox == "François vergne":
    st.sidebar.write("En tant que Responsable Admin. et Financier externe, il est fréquent d’accompagner mes clients sur la thématique des véhicules (de fonction, de service, de transport). Pour eux, il s'agit d'une problématique complexe : ils doivent équilibrer les avantages et les inconvénients entre la hausse des prix des véhicules, l’accessibilité aux différents types de carburant, les nouvelles réglementations environnementales (ex: obligation de renouveler au moins 10 % de leurs véhicules chaque année avec des véhicules à faibles émissions)  et les enjeux RSE (reporting CSRD, marque-employeur, amélioration de l’image de l’entreprise pour faciliter le recrutement, etc…).")
   
 

#Début des pages: 
if page == pages[0]:
    st.title("Introduction")
    st.header("🌍 **Bienvenue dans l'aventure écolo-automobile** !🚗💨")
    st.write(" Vous êtes prêt à plonger dans un projet captivant qui fusionne technologie, environnement et innovation ? Alors attachez vos ceintures ! Nous sommes sur le point d'explorer un sujet brûlant et d'actualité : les émissions de CO2 des véhicules. À l'ère où chaque gramme de CO2 compte dans la lutte contre le changement climatique, notre projet s'inscrit parfaitement dans cette démarche mondiale pour un avenir plus vert et durable.")
    st.subheader("🌱**CO2, Environnement et Nous : Le Défi du Siècle**")
    st.write("Les émissions de dioxyde de carbone (CO2) sont au cœur des préoccupations environnementales actuelles. Saviez-vous que les véhicules que nous conduisons quotidiennement jouent un rôle majeur dans ces émissions ? Avec l'Agence de l'Environnement et de la Maîtrise de l'Énergie (ADEME) en France, en collaboration avec l'Union Technique de l'Automobile du motocycle et du Cycle (UTAC), nous disposons d'un trésor de données collectées depuis 2001 sur les caractéristiques techniques des véhicules, leurs consommations de carburant et leurs émissions polluantes.")
    st.subheader("🚘 **Zoom sur les Caractéristiques Techniques : Quels Véhicules Polluent le Plus ?**")
    st.write("Des moteurs turbo puissants aux carrosseries aérodynamiques, en passant par les types de carburant utilisés, chaque détail compte ! Par exemple, la cylindrée du moteur, le poids du véhicule, et même le type de transmission peuvent tous influencer les niveaux d'émissions de CO2. Grâce à notre analyse de ce vaste jeu de données de 2013, nous allons dénicher les véhicules les plus gourmands en CO2, prédire les futures tendances de pollution, et comprendre quels éléments techniques exacerbent ces émissions.")
    st.subheader("🔍 **Pourquoi Tout Cela Est-il Excitant ?**")
    st.write("Imaginez pouvoir anticiper la pollution des futurs modèles de voitures avant même qu'ils ne soient sur le marché ! Nos analyses ne sont pas seulement académiques ; elles ont le potentiel de transformer les politiques environnementales et de guider des choix de consommation plus verts. En identifiant les véhicules les plus polluants et en comprenant les caractéristiques qui amplifient ces émissions, nous contribuons à un avenir où chaque choix de véhicule peut être plus conscient et durable.")
    st.subheader("🎉 **Rejoignez-nous dans cette Exploration Dynamique !**")
    st.write("Préparez-vous à une exploration riche en découvertes et en données. Ensemble, décryptons les secrets des véhicules et contribuons à réduire notre empreinte carbone. Chaque petit pas compte, et ce projet est notre façon de rouler vers un avenir plus propre et plus respectueux de notre planète.")
    st.header("**Alors, prêt à embarquer dans cette aventure écolo ?** 🚀🌿")
   
if page == pages[1]:
    st.title("Contexte du Projet")
    st.write("**Les projets : Identifier les véhicules qui émettent le plus de CO2 est important pour identifier les caractéristiques techniques qui jouent un rôle dans la pollution. Prédire à l’avance cette pollution permet de prévenir dans le cas de l’apparition de nouveaux types de véhicules (nouvelles séries de voitures par exemple)**")
    st.image("https://gcft.fr/wp-content/uploads/2017/02/ademe-logo.jpg", caption = "Logo de l'ADEME", width = 200)
    st.write("L'Agence de l'Environnement et de la Maîtrise de l'Energie (ADEME) est une institution clé en France, jouant un rôle majeur dans la promotion de pratiques respectueuses de l'environnement et dans la gestion des ressources énergétiques. Chaque année depuis 2001, l'ADEME collecte des données sur les véhicules commercialisés en France, en partenariat avec l'Union Technique de l'Automobile du motocycle et du Cycle (UTAC), organisme responsable de l'homologation des véhicules.")
    st.write("Le jeu de données : https://www.data.gouv.fr/fr/datasets/emissions-de-co2-et-de-polluants-des-vehicules-commercialises-en-france/#_")
    st.write("Ce jeu de données de 2013 offre une mine d'informations précieuses, notamment les caractéristiques techniques des véhicules, les consommations de carburant, les émissions de dioxyde de carbone (CO2) et les émissions de polluants de l'air, conforme à la norme Euro en vigueur. Ces données sont essentielles pour identifier les véhicules les plus émetteurs de CO2 et les plus polluants, ce qui permet de comprendre les caractéristiques techniques influant sur la pollution.")
    st.write("Grâce à ce jeu de données, il est possible d'entreprendre diverses analyses, telles que l'identification des véhicules les plus émetteurs de CO2, la prédiction de la pollution pour de nouveaux types de véhicules, ou encore l'évaluation de l'impact des caractéristiques techniques sur les émissions polluantes. Ces analyses peuvent contribuer à orienter les politiques environnementales et à promouvoir des choix de consommation plus durables dans le secteur automobile.")
    st.header("Notre équipe :")
    st.write("### Projet réalisé par François Vergne, Drazen Saric & Arnaud Colombel")
    st.warning("Une description de nous se trouve sur la gauche de la page.")
    
if page == pages[2]:
    st.title("Exploration des données")
    st.write("Voici un échantillon des données brutes utilisées dans notre analyse. Les 20 premières lignes du jeu de données sont affichées ci-dessous :")
    st.dataframe(donnees2013.head(20))
    st.write("### Statistiques Descriptives des Données")
    st.write("Les statistiques descriptives ci-dessous résument les principales caractéristiques des données numériques du jeu de données, telles que la moyenne, l'écart type, les valeurs minimales et maximales :")
    st.write(donnees2013.describe()) 
    buffer = io.StringIO()
    donnees2013.info(buf=buffer)
    info_str = buffer.getvalue()
    st.write("### Informations Complètes sur le Jeu de Données")
    st.write("Les informations suivantes décrivent la structure complète du jeu de données, y compris le type de chaque colonne et le nombre de valeurs manquantes (NaN). Nous remarquons qu'il y a un nombre significatif de valeurs manquantes, ce qui nécessitera une attention particulière pour le traitement des données :")
    st.text(info_str)
    st.write("")
    if st.button("Certains noms de colonne ont des désignations techniques, souhaitez-vous connaitre la désignation de chacune ?"):
        st.write("**Marque**: Le fabricant du véhicule.")
        st.write("**Modèle dossier**: Nom du modèle de véhicule dans le dossier.")
        st.write("**Modèle UTAC**: Nom du modèle de véhicule selon l'UTAC.")
        st.write("**Désignation commerciale**: Dénomination commerciale du véhicule.")
        st.write("**CNIT**: Numéro d'identification du véhicule.")
        st.write("**Type Variante Version (TVV)**: Classification du type de variante et version du véhicule.")
        st.write("**Carburant**: Type de carburant utilisé par le véhicule.")
        st.write("**Hybride**: Indique si le véhicule est hybride ou non.")
        st.write("**Puissance administrative**: Puissance administrative du véhicule en chevaux fiscaux.")
        st.write("**Puissance maximale (kW)**: Puissance maximale du véhicule en kilowatts.")
        st.write("**Boîte de vitesse**: Type de boîte de vitesse du véhicule.")
        st.write("**Consommation urbaine (l/100km)**: Consommation de carburant en milieu urbain en litres pour 100 kilomètres.")
        st.write("**Consommation extra-urbaine (l/100km)**: Consommation de carburant hors agglomération en litres pour 100 kilomètres.")
        st.write("**Consommation mixte (l/100km)**: Consommation de carburant mixte en litres pour 100 kilomètres.")
        st.write("**CO2 (g/km)**: Émissions de dioxyde de carbone par kilomètre parcouru.")
        st.write("**CO type I (g/km)**: Émissions de monoxyde de carbone de type I par kilomètre parcouru.")
        st.write("**HC (g/km)**: Émissions d'hydrocarbures par kilomètre parcouru.")
        st.write("**NOX (g/km)**: Émissions d'oxydes d'azote par kilomètre parcouru.")
        st.write("**HC+NOX (g/km)**: Émissions combinées d'hydrocarbures et d'oxydes d'azote par kilomètre parcouru.")
        st.write("**Particules (g/km)**: Émissions de particules par kilomètre parcouru.")
        st.write("**masse vide euro min (kg)**: Masse vide minimale du véhicule en kilogrammes selon la norme euro.")
        st.write("**masse vide euro max (kg)**: Masse vide maximale du véhicule en kilogrammes selon la norme euro.")
        st.write("**Norme UE**: Le champ V9 carte grise indique la norme Euro du véhicule.La norme Euro est un système de classification des moteurs qui se base sur les émissions de polluants.")
        st.write("**Date de mise à jour**: Date de la dernière mise à jour des données.")
        st.write("**Carrosserie**: Type de carrosserie du véhicule.")
        st.write("**gamme**: Gamme du véhicule.")
        if st.button("Fermer la liste des colonnes"):
            st.write()
    if st.button("Les types de carburant ont une codification, souhaitez-vous la voir ?"):
        st.write("**ES**: Essence.")
        st.write("**GO**: Diesel (gazole).")
        st.write("**EH**: Véhicule hybride non rechargeable.")
        st.write("**EE**: Essence-électricité (hybride rechargeable).")
        st.write("**EL**: Électricité.")
        st.write("**GH**: Diesel-électricité non rechargeable.")
        st.write("**ES/GP**: Essence-GPL.")
        st.write("**GP/ES**: Essence-GPL.")
        st.write("**ES/GN**: Essence-gaz naturel.")
        st.write("**GN/ES**: Essence-gaz naturel.")
        st.write("**FE**: Superéthanol E85.")
        st.write("**GN**: Gaz naturel.")
        st.write("**GL**: Diesel-électricité rechargeable.")
        if st.button("Fermer la liste des carburants"):
            st.write()
    st.write(" ")
    st.write("## Biais du Dataset")
    st.write("""
    - **Ancienneté des données :** Le jeu de données date de 2013, les données ne sont plus dans les standards actuels.
    - **Faux NaN :** Certaines valeurs NaN sont en réalité des valeurs zéro, par exemple pour les véhicules électriques.
    - **Doublons :** Présence de vrais et faux doublons dans les données.
    - **Déséquilibre des données :** Le jeu de données est fortement déséquilibré avec 83% des véhicules étant des Mercedes.
    - **Valeurs aberrantes :** Certaines entrées dans la variable 'Marque' ne sont pas des marques valides (ex : Quatro, Renault Tech).
    - **Valeurs extrêmes :** Nécessité de consulter des experts pour valider certaines valeurs techniques.
    """)
    st.write(" ")
    st.title("Pre-processing et feature engineering")
    st.write("### Étape 1 : Traitement de Nom de Variable")
    st.write("""
    - **Transformation de majuscules :** Conversion des noms de variables en majuscules pour uniformiser le jeu de données.
    - **Modification d’un nom de variable :** Changement de certains noms de variables pour une meilleure clarté et compréhension.
    """)
    st.write("### Étape 2 : Conversion en Format de Date")
    st.write("""
    - **Format de date :** Une variable était une date au format (mm/aa). Cette variable a été convertie au format de date approprié.
    """)
    st.write("### Étape 3 : Gestion des Doublons")
    st.write("""
    - **Identification des doublons :** Le jeu de données contient 619 doublons. Il est crucial de déterminer s'ils sont de vrais doublons ou non.
    - **Recommandations :**
    - **Identification :** Définir des critères pour identifier les vrais doublons.
    - **Gestion :** Supprimer ou combiner les doublons en fonction de leur impact sur les analyses.
    """)
    st.write("### Étape 4 : Gestion des NaN")
    st.write("""
    - **Reconstitution de HC, NOX ou HC+NOX :** Lorsque 2 des 3 colonnes sont connues.
    - **Véhicules électriques :**
      Remplissage des NaN par 0 pour les colonnes CO2, CO TYPE I, HC, NOX, HC+NOX et PARTICULES.
      Remplissage des NaN par 0 pour les colonnes liées aux consommations (urbaine, mixte, extra-urbaine).
    - **Véhicules Essence-électricité (hybride rechargeable) :**
      En Urbain : 100% en électrique donc 0.
      En Extra-Urbain : 5,5L (d'après les sites et commentaires, c'est entre 5,2L et 6L pour les 3 véhicules).
    - **Autres NaN :**
      Remplacement des NaN de CO TYPE I, HC, NOX, HC+NOX et PARTICULES par la médiane en fonction du carburant.
      Remplacement des NaN dans la colonne PARTICULES par la médiane.
    """)
    st.write("### Étape 5 : Encodage des Données")
    st.write("""
    - **Utilisation de OrdinalEncoder :** En attribuant des valeurs numériques ordonnées, il permet de préserver la relation hiérarchique entre les catégories.
    - **Analyse de corrélation :** Cela nous permet d'analyser la corrélation entre les variables à l'aide d'une heatmap et de formater le jeu de données pour les étapes ultérieures du machine learning.
    """)
    st.write("### Étape 6 : Standardisation (Normalisation Z-Score)")
    st.write("""
    - **Utilisation de StandardScaler :** Permet de normaliser les caractéristiques de nos données en les recentrant autour de 0 avec une variance de 1.
    - **Importance :** Cette normalisation est cruciale lorsque les caractéristiques des données ont des échelles différentes. Cela garantit que notre modèle de machine learning fonctionne efficacement et de manière optimale.
    """)

# Prétraitement et encodage avec cache
@st.cache_resource
def preprocess_and_encode(donnees2013):        
    #Gestion des Nan
    donnees2013 = donnees2013.rename(columns=lambda x: x.upper())
    donnees2013 = donnees2013.rename({'CHAMP V9': 'NORME UE'}, axis = 1)
    # Reconstitution de HC, NOX ou HC+NOX lorsque 2 des 3 colonnes sont connues
    select_col = ['HC (G/KM)', 'NOX (G/KM)', 'HC+NOX (G/KM)']
    select_donnees = donnees2013[donnees2013.isna().any(axis=1)][select_col]
    donnees2013.loc[donnees2013['HC+NOX (G/KM)'].isna(), 'HC+NOX (G/KM)'] = (select_donnees['HC (G/KM)'] + select_donnees['NOX (G/KM)'])
    donnees2013.loc[donnees2013['HC (G/KM)'].isna(), 'HC (G/KM)'] = (select_donnees['HC+NOX (G/KM)'] - select_donnees['NOX (G/KM)'])
    donnees2013.loc[donnees2013['HC+NOX (G/KM)'].isna(), 'NOX (G/KM)'] = (select_donnees['HC+NOX (G/KM)'] - select_donnees['HC (G/KM)'])

    #Pour les véhicules électriques, remplissage de NaN par 0 pour les colonnes CO2, CO TYPE I, HC, NOX, HC+NOX et PARTICULES
    donnees2013.loc[donnees2013['CARBURANT'] == 'EL', 'CO2 (G/KM)'] = donnees2013[donnees2013['CARBURANT'] == 'EL']['CO2 (G/KM)'].fillna(0)
    donnees2013.loc[donnees2013['CARBURANT'] == 'EL', 'CO TYPE I (G/KM)'] = donnees2013[donnees2013['CARBURANT'] == 'EL']['CO2 (G/KM)'].fillna(0)
    donnees2013.loc[donnees2013['CARBURANT'] == 'EL', 'HC (G/KM)'] = donnees2013[donnees2013['CARBURANT'] == 'EL']['HC (G/KM)'].fillna(0)
    donnees2013.loc[donnees2013['CARBURANT'] == 'EL', 'NOX (G/KM)'] = donnees2013[donnees2013['CARBURANT'] == 'EL']['NOX (G/KM)'].fillna(0)
    donnees2013.loc[donnees2013['CARBURANT'] == 'EL', 'HC+NOX (G/KM)'] = donnees2013[donnees2013['CARBURANT'] == 'EL']['HC+NOX (G/KM)'].fillna(0)
    donnees2013.loc[donnees2013['CARBURANT'] == 'EL', 'PARTICULES (G/KM)'] = donnees2013[donnees2013['CARBURANT'] == 'EL']['PARTICULES (G/KM)'].fillna(0)

    #Pour les véhicules électriques, remplissage de NaN par 0 pour les colonnes liées aux consommations (urbaine, mixte, extra-urbaine)
    donnees2013.loc[donnees2013['CARBURANT'] == 'EL', 'CONSOMMATION URBAINE (L/100KM)'] = donnees2013[donnees2013['CARBURANT'] == 'EL']['CONSOMMATION URBAINE (L/100KM)'].fillna(0)
    donnees2013.loc[donnees2013['CARBURANT'] == 'EL', 'CONSOMMATION EXTRA-URBAINE (L/100KM)'] = donnees2013[donnees2013['CARBURANT'] == 'EL']['CONSOMMATION EXTRA-URBAINE (L/100KM)'].fillna(0)
    donnees2013.loc[donnees2013['CARBURANT'] == 'EL', 'CONSOMMATION MIXTE (L/100KM)'] = donnees2013[donnees2013['CARBURANT'] == 'EL']['CONSOMMATION MIXTE (L/100KM)'].fillna(0)

    #Pour les véhicules Essence-électricité (hybride rechargeable), il y a 3 lignes :
    # On considère qu'en Urbain => 100% en électrique donc 0
    # On considère qu'en Extra-Urbain => 5,5L (d'après les sites et commentaires, c'est entre 5,2L et 6L pour les 3 véhicules)
    donnees2013.loc[donnees2013['CARBURANT'] == 'EE', 'CONSOMMATION URBAINE (L/100KM)'] = donnees2013[donnees2013['CARBURANT'] == 'EE']['CONSOMMATION URBAINE (L/100KM)'].fillna(0)
    donnees2013.loc[donnees2013['CARBURANT'] == 'EE', 'CONSOMMATION EXTRA-URBAINE (L/100KM)'] = donnees2013[donnees2013['CARBURANT'] == 'EE']['CONSOMMATION EXTRA-URBAINE (L/100KM)'].fillna(5.5)

    #Remplacer les NaN de 'CO TYPE I (G/KM)' par la médiane en fonction du carburant
    for carb in donnees2013.loc[donnees2013[['CO TYPE I (G/KM)']].isna().all(axis=1)]['CARBURANT'].unique():
        donnees2013.loc[(donnees2013['CO TYPE I (G/KM)'].isna()) & (donnees2013['CARBURANT'] == carb), ['CO TYPE I (G/KM)']] = donnees2013.loc[(donnees2013['CO TYPE I (G/KM)'].isna()) & (donnees2013['CARBURANT'] == carb), ['CO TYPE I (G/KM)']].fillna(donnees2013[donnees2013['CARBURANT'] == carb][['CO TYPE I (G/KM)']].median())

    #Remplacer les NaN de 'HC (G/KM)' par la médiane en fonction du carburant
    for carb in donnees2013.loc[donnees2013[['HC (G/KM)']].isna().all(axis=1)]['CARBURANT'].unique():
        donnees2013.loc[(donnees2013['HC (G/KM)'].isna()) & (donnees2013['CARBURANT'] == carb), ['HC (G/KM)']] = donnees2013.loc[(donnees2013['HC (G/KM)'].isna()) & (donnees2013['CARBURANT'] == carb), ['HC (G/KM)']].fillna(donnees2013[donnees2013['CARBURANT'] == carb][['HC (G/KM)']].median())

    #Remplacer les NaN de 'NOX (G/KM)' par la médiane en fonction du carburant
    for carb in donnees2013.loc[donnees2013[['NOX (G/KM)']].isna().all(axis=1)]['CARBURANT'].unique():
        donnees2013.loc[(donnees2013['NOX (G/KM)'].isna()) & (donnees2013['CARBURANT'] == carb), ['NOX (G/KM)']] = donnees2013.loc[(donnees2013['NOX (G/KM)'].isna()) & ( donnees2013['CARBURANT'] == carb), ['NOX (G/KM)']].fillna(donnees2013[donnees2013['CARBURANT'] == carb][['NOX (G/KM)']].median())

    #Remplacer les NaN de 'HC+NOX (G/KM)' par la médiane en fonction du carburant
    for carb in donnees2013.loc[donnees2013[['HC+NOX (G/KM)']].isna().all(axis=1)]['CARBURANT'].unique():
        donnees2013.loc[(donnees2013['HC+NOX (G/KM)'].isna()) & (donnees2013['CARBURANT'] == carb), ['HC+NOX (G/KM)']] = donnees2013.loc[(donnees2013['HC+NOX (G/KM)'].isna()) & (donnees2013['CARBURANT'] == carb), ['HC+NOX (G/KM)']].fillna(donnees2013[donnees2013['CARBURANT'] == carb][['HC+NOX (G/KM)']].median())

    #Remplacer les NaN de 'PARTICULES (G/KM)' par la médiane en fonction du carburant
    for carb in donnees2013.loc[donnees2013[['PARTICULES (G/KM)']].isna().all(axis=1)]['CARBURANT'].unique():
        donnees2013.loc[(donnees2013['PARTICULES (G/KM)'].isna()) & (donnees2013['CARBURANT'] == carb), ['PARTICULES (G/KM)']] = donnees2013.loc[(donnees2013['PARTICULES (G/KM)'].isna()) & (donnees2013['CARBURANT'] == carb), ['PARTICULES (G/KM)']].fillna(donnees2013[donnees2013['CARBURANT'] == carb][['PARTICULES (G/KM)']].median())

    #Remplacer les NaN restant sur la colonne 'PARTICULES (G/KM)' par la médiane sachant que sur 43% des reponses sont 0 et 40% sont 0,001
    donnees2013.loc[(donnees2013['PARTICULES (G/KM)'].isna()), ['PARTICULES (G/KM)']] = donnees2013.loc[(donnees2013['PARTICULES (G/KM)'].isna()), ['PARTICULES (G/KM)']].fillna(donnees2013['PARTICULES (G/KM)'].median())
       
    #Entrainement du modèle en dehors de la page pour avoir les mêmes données en la modélisation 1 et 2
    #Nettoyage du nombre de colonne
    donnees2013_ml = donnees2013.drop([
        'MARQUE',
        'MODÈLE DOSSIER',
        'MODÈLE UTAC',
        'DÉSIGNATION COMMERCIALE',
        'CNIT',
        'TYPE VARIANTE VERSION (TVV)',
        'BOÎTE DE VITESSE',
        'CO TYPE I (G/KM)',
        'HC (G/KM)',
        'NOX (G/KM)',
        'HC+NOX (G/KM)',
        'PARTICULES (G/KM)',
        'NORME UE',
        'DATE DE MISE À JOUR'
    ], axis=1)

    #Isoler la valeur cible
    y = donnees2013_ml['CO2 (G/KM)']
    X = donnees2013_ml.drop(['CO2 (G/KM)'], axis = 1)

    #Séparation du jeu de donnée pour l'entrainement et le test. On garde 20% des données pour les tests.
    from sklearn.model_selection import train_test_split

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

    from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder

    #utilisation du OneHotEncoder pour la varbiable 'Hybride' car c'est une variable binaire
    ohe = OneHotEncoder(drop='first', sparse_output=False, handle_unknown='ignore')
    cat_hybride_train = ohe.fit_transform(X_train[['HYBRIDE']])
    cat_hybride_test = ohe.transform(X_test[['HYBRIDE']])

    # Encodage de 'CARBURANT', 'CARROSSERIE', 'GAMME' avec OrdinalEncoder
    oe = OrdinalEncoder(handle_unknown='use_encoded_value', unknown_value=-1)
    cat_oe = ['CARBURANT', 'CARROSSERIE', 'GAMME']
    cat_oe_train = oe.fit_transform(X_train[cat_oe])
    cat_oe_test = oe.transform(X_test[cat_oe])


    # Concaténer les colonnes encodées avec les autres colonnes
    X_train = pd.concat([
        pd.DataFrame(cat_hybride_train, index=X_train.index, columns=['HYBRIDE']),
        pd.DataFrame(cat_oe_train, index=X_train.index, columns=['CARBURANT', 'CARROSSERIE', 'GAMME']),
        X_train.drop(['HYBRIDE', 'CARBURANT', 'CARROSSERIE', 'GAMME'], axis=1)], axis=1)


    X_test = pd.concat([
        pd.DataFrame(cat_hybride_test, index=X_test.index, columns=['HYBRIDE']),
        pd.DataFrame(cat_oe_test, index=X_test.index, columns=['CARBURANT', 'CARROSSERIE', 'GAMME']),
        X_test.drop(['HYBRIDE','CARBURANT', 'CARROSSERIE', 'GAMME'], axis=1)], axis=1)


    #Le StandardScaler nous permet d'appliquer la transformation Z-Score à nos données.
    from sklearn.preprocessing import StandardScaler
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)

    return X_train, X_test, y_train, y_test, ohe, oe, sc, cat_oe, donnees2013, donnees2013_ml

X_train, X_test, y_train, y_test, ohe, oe, sc, cat_oe, donnees2013, donnees2013_ml = preprocess_and_encode(donnees2013)

if page == pages[3]:
    st.write("## Observons les données grâce à la Data Visualisation")
    st.write("### DataViz n°1")
    fig = px.histogram(donnees2013, x='CO2 (G/KM)', title='Distribution des émissions de CO2')
    fig.update_layout(xaxis_title='CO2 (G/KM)', yaxis_title='Count', bargap=0.2, template='plotly_white')
    st.plotly_chart(fig)
    
    
    st.write("### DataViz N°2")
    st.write("Cette visualisation montre la distribution des émissions de CO2 en fonction des différents types de carburants, révélant que les véhicules utilisant le carburant ES (Essence) et FE (Flexible Fuel) ont une large gamme d'émissions, tandis que les carburants comme EE (Electricité) et GL (Gaz Liquéfié) ont des émissions significativement plus faibles. Les types de carburants GH (Hybride), EH (Hybride Essence), et GN (Gaz Naturel) affichent des distributions plus restreintes, indiquant une performance environnementale plus homogène dans ces catégories.")
    plt.figure(figsize=(10, 6))
    sns.violinplot(x='CARBURANT', y='CO2 (G/KM)', data = donnees2013, palette='Set2')
    plt.title('Distribution des émissions de CO2 par type de carburant')
    plt.xlabel('Type de carburant')
    plt.ylabel('Émissions de CO2 (g/km)')
    plt.xticks(rotation=45)
    st.pyplot(plt)

    st.write("### DataViz N°3")
    st.write("L'analyse du nuage de points révèle que plus la puissance du moteur est élevée et plus il consomme, plus les émissions de Co2 associées sont élevées.")
    # Nettoyer les données
    data_nettoyer = donnees2013.dropna(subset=['CO2 (G/KM)'])

    # Définir les variables pour le nuage de points
    x = data_nettoyer['PUISSANCE MAXIMALE (KW)']
    y = data_nettoyer['CONSOMMATION MIXTE (L/100KM)']
    co2 = data_nettoyer['CO2 (G/KM)']

    # Créer le nuage de points avec Plotly
    fig = px.scatter(data_nettoyer, x='PUISSANCE MAXIMALE (KW)', y='CONSOMMATION MIXTE (L/100KM)',
                    color='CO2 (G/KM)', color_continuous_scale='RdBu_r', 
                    title='Puissance maximale vs Consommation de carburant Vs CO2',
                    labels={'PUISSANCE MAXIMALE (KW)': 'Puissance maximale du moteur (kW)', 
                            'CONSOMMATION MIXTE (L/100KM)': 'Consommation mixte de carburant (l/100km)',
                            'CO2 (G/KM)': 'Émissions de CO2 (g/km)'})

    # Ajouter une régression linéaire
    X = x.values.reshape(-1, 1)
    reg = LinearRegression().fit(X, y)
    data_nettoyer['Regression Line'] = reg.predict(X)

    fig.add_trace(go.Scatter(
        x=data_nettoyer['PUISSANCE MAXIMALE (KW)'],
        y=data_nettoyer['Regression Line'],
        mode='lines',
        name='Ligne de régression',
        line=dict(color='gray')
    ))

    # Afficher le graphique dans Streamlit
    st.plotly_chart(fig)

    st.write("### DataViz N°4")
    co2_by_marque = donnees2013.groupby('MARQUE')['CO2 (G/KM)'].mean().sort_values()
    co2_by_marque = donnees2013.groupby('MARQUE')['CO2 (G/KM)'].mean().sort_values().reset_index()
    fig = px.bar(co2_by_marque, x='CO2 (G/KM)', y='MARQUE', orientation='h',
                title='Comparaison des émissions de CO2 par marque de véhicule',
                labels={'CO2 (G/KM)': 'Émissions de CO2 moyennes (g/km)', 'MARQUE': 'Marque'},
                color_discrete_sequence=['skyblue'])
    fig.update_layout(xaxis=dict(showgrid=True, gridcolor='LightGrey'))
    st.plotly_chart(fig)

    st.write("### DataViz N°5")
    st.write("Nous observons sur ce graphique une corrélation entre la masse du véhicule et les émissions de CO2")
    fig = px.scatter(donnees2013, x='MASSE VIDE EURO MAX (KG)', y='CO2 (G/KM)', 
                 title="Relation entre les émissions de CO2 (G/KM) et la masse des véhicules",
                 labels={'MASSE VIDE EURO MAX (KG)': 'Masse des véhicules (KG)', 'CO2 (G/KM)': 'Émissions de CO2 (G/KM)'},
                 color_discrete_sequence=['#A7001E'], width=2000, height=800)

    fig.update_traces(marker=dict(size=6))
    st.plotly_chart(fig)

    st.write("### DataViz N°6")
    st.write("Ce graphique permet d'observer la corrélation entre les différentes variables. Si nous analysons la variable CO2 (g/km), nous remarquons que les variables les plus corrélées sont les 3 variables de consommations (mixte, urbaine et extra-urbaine), ensuite, la masse du véhicule est aussi très important (0.75 et 0.75 de coefficient) puis arrive ensuite, le modèle (dossier et UTAC) puis le type de carrosserie. Ce grpahique nous confirme l'analyse précédente sur la corrélation entre le type de carburant et les émissions de NOX.")
    oe = OrdinalEncoder()
    # Encodage des données 2013 et reconstruction en df
    donnees2013_cor = oe.fit_transform(donnees2013)
    donnees2013_cor  = pd.DataFrame(donnees2013_cor, columns=donnees2013.columns)

    # corrélation
    correlation_matrix = donnees2013_cor.corr()
    fig = px.imshow(correlation_matrix, text_auto=True, color_continuous_scale='turbo', aspect='auto')
    fig.update_layout(title='Matrice de corrélation', width=4000, height=1000)
    st.plotly_chart(fig)

    st.write("### DataViz bonus")
    st.write("Nous finissons notre datavisualisation sur ce graphique afin d'attirer l'attention sur un déséquilibre du jeu de données. En effet, nous remarquons sans difficulté que 2 types de carburant ont le monopole. Le Gasoil pour 84,2% et l'Essence pour 13,7%.")
    carburant_counts = donnees2013['CARBURANT'].value_counts()
    carburant_counts_df = carburant_counts.reset_index()
    carburant_counts_df.columns = ['CARBURANT', 'COUNT']
    fig = px.pie(carburant_counts_df, values='COUNT', names='CARBURANT', title='Répartition des véhicules par type de carburant')
    st.plotly_chart(fig)

 

# Entraînement et cache des modèles
@st.cache_resource
def train_decision_tree_classifier(X_train, y_train):
    dt_clf = DecisionTreeClassifier()
    dt_clf.fit(X_train, y_train)
    return dt_clf

dt_clf = train_decision_tree_classifier(X_train, y_train)

@st.cache_resource
def train_decision_tree_regressor(X_train, y_train):
    dt_reg = DecisionTreeRegressor()
    dt_reg.fit(X_train, y_train)
    return dt_reg

dt_reg = train_decision_tree_regressor(X_train, y_train)

@st.cache_resource
def train_linear_regression(X_train, y_train):
    lr = LinearRegression()
    lr.fit(X_train, y_train)
    return lr

lr = train_linear_regression(X_train, y_train)

@st.cache_resource
def train_logistic_regression(X_train, y_train):
    logr = LogisticRegression()
    logr.fit(X_train, y_train)
    return logr

logr = train_logistic_regression(X_train, y_train)


# Sauvegarde du modèle avec Joblib
joblib.dump(dt_clf, 'dt_clf_model.pkl')
joblib.dump(dt_reg, 'dt_reg_model.pkl')
joblib.dump(lr, 'lr_model.pkl')
joblib.dump(logr, 'logr_model.pkl')

# Chargement du modèle
dt_clf = joblib.load('dt_clf_model.pkl')
dt_reg = joblib.load('dt_reg_model.pkl')
lr = joblib.load('lr_model.pkl')
logr = joblib.load('logr_model.pkl')


# Calcul des scores pour chaque modèle après l'entraînement

# Pour l'arbre de décision
train_score_clf = round(dt_clf.score(X_train, y_train),4)
test_score_clf = round(dt_clf.score(X_test, y_test),4)

# Pour l'arbre de régression
train_score_reg = round(dt_reg.score(X_train, y_train),4)
test_score_reg = round(dt_reg.score(X_test, y_test),4)

# Pour la régression linéaire
train_score_lr = round(lr.score(X_train, y_train),4)
test_score_lr = round(lr.score(X_test, y_test),4)

# Pour la régression logistique
train_score_logr = round(logr.score(X_train, y_train),4)
test_score_logr = round(logr.score(X_test, y_test),4)

# Calcul des métriques pour les modèles
def calculate_metrics(_model, X_test, y_test):
    y_pred = _model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    return mae, mse, rmse, y_pred

mae_clf, mse_clf, rmse_clf, y_pred_test_clf = calculate_metrics(dt_clf, X_test, y_test)
mae_reg, mse_reg, rmse_reg, y_pred_test_reg = calculate_metrics(dt_reg, X_test, y_test)
mae_lr, mse_lr, rmse_lr, y_pred_test_lr = calculate_metrics(lr, X_test, y_test)
mae_logr, mse_logr, rmse_logr, y_pred_test_logr = calculate_metrics(logr, X_test, y_test)
 
#97% à 98% des données ont un carburant 'ES' ou 'GO'. On prépare donc un test pour observer les résultats sur les données en déhors de ces 2 types de carburant.
#Nous allons réperer les 2 valeurs ayant un nombre d'occurences élevé pour repérer les 'ES' et 'GO' pour ensuite les enlever dans notre comparaison de y_test et y_pred_test
# Calcul des métriques pour les modèles


def calculate_metrics_horsGOES(_model, X_test, y_test):
    # Obtenir les valeurs uniques et leurs occurrences pour la deuxième colonne de X_test
    valeurs_uniques, nombre_occurrences = np.unique(X_test[:, 1], return_counts=True)

    # Trouver les deux valeurs avec les occurrences les plus élevées
    indices_top2 = np.argsort(nombre_occurrences)[-2:]
    valeurs_top2 = valeurs_uniques[indices_top2]

    # Filtrer X_test pour exclure ces deux valeurs
    ind_x_test_horsGOES = np.where((X_test[:, 1] != valeurs_top2[0]) & (X_test[:, 1] != valeurs_top2[1]))[0]

    # Extraire les lignes spécifiques de X_test
    X_test_horsGOES = X_test[ind_x_test_horsGOES]

    # Convertir y_test en numpy array pour éviter les problèmes d'index
    y_test_array = y_test.to_numpy()

    # Extraire les valeurs correspondantes de y_test
    y_test_horsGOES = y_test_array[ind_x_test_horsGOES]

    # Prédire les valeurs pour X_test_horsGOES avec le modèle donné
    y_pred_horsGOES = _model.predict(X_test_horsGOES)

    # Calcul des métriques
    mae_horsGOES = mean_absolute_error(y_test_horsGOES, y_pred_horsGOES)
    mse_horsGOES = mean_squared_error(y_test_horsGOES, y_pred_horsGOES)
    rmse_horsGOES = np.sqrt(mse_horsGOES)

    return mae_horsGOES, mse_horsGOES, rmse_horsGOES

# Calcul des métriques hors 'ES' et 'GO' pour chaque modèle
mae_clf_horsGOES, mse_clf_horsGOES, rmse_clf_horsGOES = calculate_metrics_horsGOES(dt_clf, X_test, y_test)
mae_reg_horsGOES, mse_reg_horsGOES, rmse_reg_horsGOES = calculate_metrics_horsGOES(dt_reg, X_test, y_test)
mae_lr_horsGOES, mse_lr_horsGOES, rmse_lr_horsGOES = calculate_metrics_horsGOES(lr, X_test, y_test)
mae_logr_horsGOES, mse_logr_horsGOES, rmse_logr_horsGOES = calculate_metrics_horsGOES(logr, X_test, y_test)

if page == pages[4]:
    st.header("Modélisation 1 et analyse de performance")
    st.warning("""
    Lors de la phase d'exploration et de datavisualisation, nous avons identifié nos variables explicatives notamment **la consommation**, **la masse du véhicule** et **le type de carburant**. Nous allons donc nettoyer notre jeu de données pour ne conserver que ces variables. De plus, nous isolerons la variable cible **'CO2 (g/km)'**. Ensuite, nous avons effectué les phases de prétraitement et d'ingénierie des caractéristiques, en réduisant le nombre de variables pour ne garder que les explicatives.

    Pour garantir un bon entraînement de notre modèle, nous allons diviser le jeu de données en deux parties : **80 % pour l'entraînement** et **20 % pour les tests**.
    """)

    st.write("Pour comparer les modèles, la Mean Absolute Error (MAE) a été choisie comme métrique principale. Elle a été sélectionnée pour plusieurs raisons. Tout d'abord, son interprétabilité : la MAE a la même unité que la variable cible (g/km de CO2), ce qui permet de comprendre directement l'ampleur des erreurs de prédiction. De plus, elle est moins sensible aux grandes erreurs de prédiction par rapport à la Mean Squared Error (MSE), ce qui la rend plus robuste aux outliers. Pour obtenir une évaluation complète du modèle, d'autres métriques de performance ont également été utilisées. La Mean Squared Error (MSE) calcule la moyenne des différences mises au carré entre les vraies valeurs et les valeurs prédites. Bien que moins interprétable que la MAE, elle pénalise davantage les grandes erreurs, ce qui peut être utile pour certaines applications. La Root Mean Squared Error (RMSE), qui est la racine carrée de la MSE, combine les avantages de la MSE et de l'interprétabilité car elle a la même unité que la variable cible. Ces métriques supplémentaires ont permis de mieux comprendre les performances globales du modèle.")
    st.write("Mean Absolute Error (MAE) : C'est la moyenne des différences absolues entre les vraies valeurs et les valeurs prédites du modèle. Elle est facilement interprétable au regard de la variable cible, car elle a la même unité.")
    st.write("Mean Squared Error (MSE) : C'est la moyenne des différences mises au carré entre les vraies valeurs et les valeurs prédites de la variable cible. Elle n'est pas dans la même unité que la variable cible, ce qui rend son interprétation plus complexe. Cette métrique pénalise davantage les grandes erreurs que la MAE. Elle est donc intéressante lorsque nous souhaitons absolument éviter ces cas.")
    st.write("Root Mean Squared Error (RMSE) : C'est la racine carrée de la Mean Squared Error. Elle pénalise également davantage les grands écarts de prédiction. Elle a la même unité que la variable cible donc elle sera plus interprétable que la MSE.")
    st.warning("""
    97% à 98% des données ont un carburant 'ES' ou 'GO'. Si nos modèles sont très performant pour ces 2 types de carburant, ils auront des scores proches de 97% à 98% de bonnes réponses.
    Or, ils peuvent donner de mauvaises prédictions sur les autres types de carburant. Donc, nous observerons aussi les métriques en excluant ces 2 types de carburant.""")

    # Affichage des résultats de l'arbre de décision dans Streamlit
    st.write("## Arbre de décision")
    st.write(f'Score sur ensemble train: {train_score_clf}')
    st.write(f'Score sur ensemble test: {test_score_clf}')
    st.write("La méthode score est une métrique qui va comparer les résultats de prédictions de votre jeu de données X par rapport à y. Nous pouvons remarquer un faible écart de score entre le jeu d'entrainement et le jeu de test. Nous ne sommes donc pas dans un cas d'overfitting. De plus, le score sur le jeu de test est proche de 1 (0,96), nous pouvons donc déduire que notre modèle est performant.")
    st.write("MAE =", round(mae_clf, 3))
    st.write("MSE =", round(mse_clf, 3))
    st.write("RMSE =", round(rmse_clf, 3))
    st.write("Observons maintenant la performance du modèle sur les véhicules n'étant pas au carburant essence ou gasoil")
    st.write("MAE =", round(mae_clf_horsGOES, 3))
    st.write("MSE =", round(mse_clf_horsGOES, 3))
    st.write("RMSE =", round(rmse_clf_horsGOES, 3))

    # Affichage des résultats de l'arbre de régression dans Streamlit
    st.write("## Arbre de régression")
    st.write(f'Score sur ensemble train: {train_score_reg}')
    st.write(f'Score sur ensemble test: {test_score_reg}')
    st.write("Encore, nous pouvons remarquer un faible écart de score entre le jeu d'entrainement et le jeu de test. La performance est aussi très bonne.")
    st.write("MAE =", round(mae_reg, 3))
    st.write("MSE =", round(mse_reg, 3))
    st.write("RMSE =", round(rmse_reg, 3))
    st.write("Observons maintenant la performance du modèle sur les véhicules n'étant pas au carburant essence ou gasoil")
    st.write("MAE =", round(mae_reg_horsGOES, 3))
    st.write("MSE =", round(mse_reg_horsGOES, 3))
    st.write("RMSE =", round(rmse_reg_horsGOES, 3))

    # Affichage des résultats de la régression linéaire dans Streamlit 
    st.write("## Régression linéaire")
    st.write(f'Score sur ensemble train: {train_score_lr}')
    st.write(f'Score sur ensemble test: {test_score_lr}')
    st.write("Encore, nous pouvons remarquer un faible écart de score entre le jeu d'entrainement et le jeu de test. La performance est aussi très bonne.")
    st.write("MAE =", round(mae_lr, 3))
    st.write("MSE =", round(mse_lr, 3))
    st.write("RMSE =", round(rmse_lr, 3))
    st.write("Observons maintenant la performance du modèle sur les véhicules n'étant pas au carburant essence ou gasoil")
    st.write("MAE =", round(mae_lr_horsGOES, 3))
    st.write("MSE =", round(mse_lr_horsGOES, 3))
    st.write("RMSE =", round(rmse_lr_horsGOES, 3))

    # Affichage des résultats de la régression logistic dans Streamlit 
    st.write("## Régression logistique")
    st.write(f'Score sur ensemble train: {train_score_logr}')
    st.write(f'Score sur ensemble test: {test_score_logr}')
    st.write("Encore, nous pouvons remarquer un faible écart de score entre le jeu d'entrainement et le jeu de test. La performance est aussi très bonne.")
    st.write("MAE =", round(mae_logr, 3))
    st.write("MSE =", round(mse_logr, 3))
    st.write("RMSE =", round(rmse_logr, 3))
    st.write("Observons maintenant la performance du modèle sur les véhicules n'étant pas au carburant essence ou gasoil")
    st.write("MAE =", round(mae_clf_horsGOES, 3))
    st.write("MSE =", round(mse_clf_horsGOES, 3))
    st.write("RMSE =", round(rmse_clf_horsGOES, 3))


    st.warning("""
    Les modèles Grid Search et XGBoost nécessitent plusieurs minutes pour se charger. C'est pourquoi nous vous offrons la possibilité de les activer uniquement à votre demande ci-dessous.
    """)
    algo_options_ml = ["Aucun Choix","Grid Search CV avec Random Forest", "Modèle XGBoost"]
    algo_selected_ml = st.selectbox("Choisir le modèle :",
                              options = algo_options_ml)
    if algo_selected_ml  == "Grid Search CV avec Random Forest":
        # Entraîner le modèle RandomForestRegressor
        rf = RandomForestRegressor(random_state=42)
        rf.fit(X_train, y_train)

        # Prédictions initiales RandomForestRegressor
        y_pred_initial = rf.predict(X_test)
    
        # Évaluation initiale RandomForestRegressor
        initial_mse = mean_squared_error(y_test, y_pred_initial)
        initial_r2 = r2_score(y_test, y_pred_initial)

        # Paramètres pour Grid Search
        param_grid = {
            'n_estimators': [10, 20, 30],
            'max_depth': [None, 10, 20, 30],
            'min_samples_split': [2, 5, 10]
        }

        # Grid Search avec validation croisée
        grid_search = GridSearchCV(estimator=rf, param_grid=param_grid, cv=5, scoring='neg_mean_squared_error', n_jobs=-1)
        grid_search.fit(X_train, y_train)

        # Meilleurs paramètres et modèle optimisé
        best_rf = grid_search.best_estimator_
        y_pred_optimized = best_rf.predict(X_test)

        # Évaluation des performances
        optimized_mse = mean_squared_error(y_test, y_pred_optimized)
        optimized_r2 = r2_score(y_test, y_pred_optimized)

        # Affichage des résultats dans Streamlit
        st.write("## Grid Search CV avec Random Forest")
        st.write("Initial Mean Squared Error:", initial_mse)
        st.write("Initial R^2 Score:", initial_r2)
        st.write("Meilleurs paramètres :", grid_search.best_params_)
        st.write("Optimized Mean Squared Error:", optimized_mse)
        st.write("Optimized R^2 Score:", optimized_r2)

    if algo_selected_ml  == "Modèle XGBoost":
        # Entraîner le modèle
        xgb_model = xgb.XGBRegressor(objective='reg:squarederror', random_state=42)
        xgb_model.fit(X_train, y_train)

        # Prédictions
        y_pred_xgb = xgb_model.predict(X_test)

        # Évaluation des performances
        xgb_mse = mean_squared_error(y_test, y_pred_xgb)
        xgb_r2 = r2_score(y_test, y_pred_xgb)

        # Affichage des résultats dans Streamlit
        st.write("## Modèle XGBoost")
        st.write("Mean Squared Error (XGBoost):", xgb_mse)
        st.write("R^2 Score (XGBoost):", xgb_r2)
    


if page == pages[5]:
        st.header("Modélisation 2 : Simulation pour un nouveau véhicule")
        
        #Choix des variables pour le véhicule "test" de notre modélisation 2
        st.write("Veuillez renseigner le type de carburant :")
        carburant = st.selectbox('CARBURANT', ['GO', 'ES']) #, 'EH', 'GP/ES', 'ES/GP', 'ES/GN', 'GN/ES', 'FE', 'GH', 'GN', 'EL', 'EE'])

        st.write("Veuillez indiquer si le véhicule est hybride :")
        hybride = st.selectbox('HYBRIDE', ['oui', 'non'])

        st.write("Veuillez entrer la puissance administrative :")
        puissance_administrative = st.slider('PUISSANCE ADMINISTRATIVE', min_value=1, max_value=10, value=1)

        st.write("Veuillez entrer la puissance maximale (KW) :")
        puissance_maximale = st.slider('PUISSANCE MAXIMALE (KW)', min_value=0.0, max_value=600.0, value=0.0)

        st.write("Veuillez entrer la consommation urbaine (L/100KM) :")
        conso_urbaine = st.slider('CONSOMMATION URBAINE (L/100KM)', min_value=0.0, max_value=50.0, value=0.0)

        st.write("Veuillez entrer la consommation extra-urbaine (L/100KM) :")
        conso_extra_urbaine = st.slider('CONSOMMATION EXTRA-URBAINE (L/100KM)', min_value=0.0, max_value=50.0, value=0.0)

        st.write("Veuillez entrer la consommation mixte (L/100KM) :")
        conso_mixte = st.slider('CONSOMMATION MIXTE (L/100KG)', min_value=0.0, max_value=50.0, value=0.0)

        st.write("Veuillez entrer la masse vide minimum (KG) :")
        masse_vide_min = st.slider('MASSE VIDE EURO MIN (KG)', min_value=0, max_value=3500, value=0)

        st.write("Veuillez entrer la masse vide maximum (KG) :")
        masse_vide_max = st.slider('MASSE VIDE EURO MAX (KG)', min_value=0, max_value=3500, value=0)

        st.write("Veuillez renseigner le type de carrosserie :")
        carrosserie = st.selectbox('CARROSSERIE', ['MINIBUS', 'BERLINE', 'COUPE', 'COMBISPACE', 'BREAK', 'TS TERRAINS/CHEMINS', 'MONOSPACE COMPACT', 'MINISPACE', 'CABRIOLET', 'MONOSPACE'])

        st.write("Veuillez renseigner la gamme du véhicule :")
        gamme = st.selectbox('GAMME', ['MOY-SUPER', 'LUXE', 'MOY-INFER', 'INFERIEURE', 'SUPERIEURE', 'ECONOMIQUE'])

        # Enregistrement dans un tableau
        donnees_mod2 = {
            'CARBURANT': [carburant],
            'HYBRIDE': [hybride],
            'PUISSANCE ADMINISTRATIVE': [puissance_administrative],
            'PUISSANCE MAXIMALE (KW)': [puissance_maximale],
            'CONSOMMATION URBAINE (L/100KM)': [conso_urbaine],
            'CONSOMMATION EXTRA-URBAINE (L/100KM)': [conso_extra_urbaine],
            'CONSOMMATION MIXTE (L/100KM)': [conso_mixte],
            'MASSE VIDE EURO MIN (KG)': [masse_vide_min],
            'MASSE VIDE EURO MAX (KG)': [masse_vide_max],
            'CARROSSERIE': [carrosserie],
            'GAMME': [gamme]
        }

        df_mod2 = pd.DataFrame(donnees_mod2)

        #utilisation du OneHotEncoder pour la varbiable 'Hybride' car c'est une variable binaire
        cat_hybride_df_mod2 = ohe.transform(df_mod2[['HYBRIDE']])

        # Encodage de 'CARBURANT', 'CARROSSERIE', 'GAMME' avec OrdinalEncoder
        cat_oe_df_mod2 = oe.transform(df_mod2[cat_oe])


        # Concaténer les colonnes encodées avec les autres colonnes
        df_mod2 = pd.concat([
            pd.DataFrame(cat_hybride_df_mod2, index=df_mod2.index, columns=['HYBRIDE']),
            pd.DataFrame(cat_oe_df_mod2, index=df_mod2.index, columns=['CARBURANT', 'CARROSSERIE', 'GAMME']),
            df_mod2.drop(['HYBRIDE','CARBURANT', 'CARROSSERIE', 'GAMME'], axis=1)], axis=1)

        algo_options = ["Arbre de décision", "Arbre de régression", "Régression linéaire","Régression logistique"]
        algo_selected = st.selectbox("Veuillez choisir un algorythme:",
                              options = algo_options)
        
        if algo_selected == "Arbre de décision":
            st.write("MAE =", round(mae_clf, 3))
            st.write("MSE =", round(mse_clf, 3))
            st.write("RMSE =", round(rmse_clf, 3))

            # Générer la prédiction
            y_pred_mod2_clf = dt_clf.predict(df_mod2)
            st.header("La prédiction d'émission de CO2 (g/km) pour un véhicule paramétré comme celui-ci est CO2 :")
            st.header(y_pred_mod2_clf[0])

        if algo_selected == "Arbre de régression":
            st.write("MAE =", round(mae_reg, 3))
            st.write("MSE =", round(mse_reg, 3))
            st.write("RMSE =", round(rmse_reg, 3))

            # Générer la prédiction
            y_pred_mod2_reg = dt_reg.predict(df_mod2)
            st.header("La prédiction d'émission de CO2 (g/km) pour un véhicule paramétré comme celui-ci est CO2 :")
            st.header(y_pred_mod2_reg[0])

        if algo_selected == "Régression linéaire":
            st.write("MAE =", round(mae_lr, 3))
            st.write("MSE =", round(mse_lr, 3))
            st.write("RMSE =", round(rmse_lr, 3))

            # Générer la prédiction
            y_pred_mod2_lr = lr.predict(df_mod2)
            st.header("La prédiction d'émission de CO2 (g/km) pour un véhicule paramétré comme celui-ci est CO2 :")
            st.header(y_pred_mod2_lr[0])

        if algo_selected == "Régression logistique":
            st.write("MAE =", round(mae_logr, 3))
            st.write("MSE =", round(mse_logr, 3))
            st.write("RMSE =", round(rmse_logr, 3))

            # Générer la prédiction
            y_pred_mod2_logr = logr.predict(df_mod2)
            st.header("La prédiction d'émission de CO2 (g/km) pour un véhicule paramétré comme celui-ci est CO2 :")
            st.header(y_pred_mod2_logr[0])
