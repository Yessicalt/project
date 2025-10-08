import streamlit as st
import pandas as pd
import plotly.express as px

data = pd.read_csv('vehicles_us.csv')

st.header("Aplicación web de analisis de datos de vehículos en EE.UU.")

st.write("1. Vista previa de Vehiculos de la marca ")
st.dataframe(data.head(500))


st.write("2. Histograma de Precios por Modelo")

# Filtro por tipo
tipos = data['type'].dropna().unique()
tipo_seleccionado = st.selectbox(
    "Selecciona el tipo de vehículo:", sorted(tipos))

# Filtrar por tipo
data_filtrado = data[data['type'] == tipo_seleccionado]

# Crear histograma
fig = px.histogram(
    data_filtrado,
    x='model',
    y='price',
    title=f'Histograma de precios por modelo ({tipo_seleccionado})',
    color='model'
)

fig.update_layout(
    xaxis_title='Model',
    yaxis_title='Price',
    bargap=0.2
)

st.plotly_chart(fig)


st.write("3. Vehiculos con mejor precio de venta en los utimos 5 años")
