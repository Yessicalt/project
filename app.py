import streamlit as st
import pandas as pd
import plotly.express as px

data = pd.read_csv('vehicles_us.csv')

st.header('Aplicación web de analisis de datos de vehículos en EE.UU.')
