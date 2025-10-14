import streamlit as st
import pandas as pd
import plotly.express as px

data = pd.read_csv('vehicles_us.csv')

st.title('Aplicación web de analisis de datos de vehículos en EE.UU.')

st.header('1. Vista previa de los datos')
st.dataframe(data.head(500))


st.header('2. Vehículos por modelo según el tipo')

hist_button = st.button('Construir histograma')  # crear un botón
if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Visualización con modelos de vehiculos existentes según su tipo.')
    st.write('Importante: Haga clic en los elementos de la leyenda para filtrar los tipos de vehículos. Al darle un clic podrá ver solo ese tipo, al darle doble clic podrá alternar la visibilidad del tipo seleccionado.')

    # Agrupamos por tipo y modelo para contar la cantidad
    conteo = (data.groupby(['type', 'model'], as_index=False).size().rename(
        columns={'size': 'cantidad'}))
    # Crear gráfico
    fig = px.bar(
        conteo,
        x='model',
        y='cantidad',
        color='type',  # cada tipo tendrá su color y su entrada en la leyenda,
    )
    # Ajustes de diseño y comportamiento
    fig.update_layout(
        xaxis_title='Modelo',
        yaxis_title='Cantidad de vehículos',
        bargap=0.2,
        height=600,
        legend_title_text='Tipo de vehículo',
        legend_itemclick='toggleothers',  # clic = deja solo ese tipo
        legend_itemdoubleclick='toggle'  # doble clic = alterna visibilidad
    )
    st.plotly_chart(fig, use_container_width=True)


st.header('3. Vehiculos con mejor precio de venta en los utimos 5 años')
hist_button = st.button('Construir gráfico de dispersión')  # crear un botón
if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write('Visualización de Gráfico de dispersión con los tipos de vehiculos con mejores precio de venta en el pasar de los años.')

    # Agrupamos por tipo y modelo para contar la cantidad
    tendencia = (data.groupby(['model_year', 'type'], as_index=False)['price'].mean()
                 .sort_values(['model_year', 'type'])
                 )

    # crear un gráfico de dispersión
    fig = px.scatter(
        tendencia,
        x='model_year',
        y='price',
        color='type',
        title='Tendencia de precios promedio por tipo de vehículo'
    )
    st.plotly_chart(fig, use_container_width=True)
