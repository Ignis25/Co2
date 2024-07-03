import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import chardet
import matplotlib.pyplot as plt

st.title("Projet Co2")
st.image("https://cdn.futura-sciences.com/buildsv6/images/wide1920/7/b/2/7b2a2ed969_96670_voiture-propre.jpg", width=300)
st.title("Émissions de CO2 et Véhicules : À la Conquête d'un Futur Plus Vert")
st.write("### Projet réalisé par François Vergne, Drazen Saric & Arnaud Colombel")

#Sidebar 
st.sidebar.title("Sommaire")
pages=["Introduction","Contexte","Exploration des données", "DataVizualization", "Modélisation"]
page=st.sidebar.radio("Naviguer vers", pages)
st.sidebar.write("\n")
st.sidebar.write("\n")
st.sidebar.write("\n")
st.sidebar.write("\n")
st.sidebar.image("https://www.nuancesdeliege.ch/wp-content/uploads/2018/08/Qui-sommes-nous.png", width = 200)


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
    st.write("Colombel Arnaud, Saric Drazen et Vergne François")
    
if page == pages[2]:
    st.title("Exploration des données")
    st.header("Voici un echantillon de notre jeu de données brutes")
    st.dataframe(donnees2013.head(20))
    st.write(donnees2013.describe()) 
    buffer = io.StringIO()
    donnees2013.info(buf=buffer)
    info_str = buffer.getvalue()
    st.text(info_str)
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

if page == pages[3]:
    st.write("### Data Visualisation")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.violinplot(x='Carburant', y='CO2 (g/km)', data=donnees2013, palette='Set2', ax=ax)
    ax.set_title("Distribution du CO2 par type de carburant")
    st.pyplot(fig)

if page == pages[4]
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
        'DATE DE MISE À JOUR',
        'année'
    ], axis=1)
    
    #Isoler la valeur cible
    y = donnees2013_ml['CO2 (G/KM)']
    X = donnees2013_ml.drop(['CO2 (G/KM)'], axis = 1)
    
    #Séparation du jeu de donnée pour l'entrainement et le test. On garde 20% des données pour les tests.
    from sklearn.model_selection import train_test_split
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)

    st.dataframe(X_train.head(30))

#Objectif pour mardi 10/07 : Arnaud => page dataviz / François => commencer code machine learning



