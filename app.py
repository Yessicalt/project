import streamlit as st
import pandas as pd
import plotly.express as px

data = pd.read_csv('vehicles_us.csv')

st.header('Aplicación web de analisis de datos de vehículos en EE.UU.')

hist_button = st.button('Construir histograma')
if hist_button:
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)
