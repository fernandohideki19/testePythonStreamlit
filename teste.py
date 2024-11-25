
import streamlit as st
import pandas as pd

st.write("""
            #Teste
         """)

df = pd.read_csv("consolidado_tratado.csv")
st.line_chart(df)