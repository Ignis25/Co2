import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

st.title("Mon premier Streamlit")
st.write("Introduction")
if st.checkbox("Afficher"):
  st.write("Suite du Streamlit")
