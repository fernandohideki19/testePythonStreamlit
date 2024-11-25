
import streamlit as st
import pandas as pd

df = pd.read_csv("consolidado_tratado.csv", delimiter=";")
st.dataframe(df)