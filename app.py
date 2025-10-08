import streamlit as st
import pandas as pd
import plotly.express as px

data = pd.read_csv('vehicles_us.csv')

st.header('Aplicación web de analisis de datos de vehículos en EE.UU.')

column = st.selectbox("Selecciona la columna para el histograma", data.columns)

hist_button = st.button('Construir histograma')
if hist_button:
    st.write(f'Creando histograma para la columna: {column}')
    fig = px.histogram(data, x=column)
    st.plotly_chart(fig, use_container_width=True)
