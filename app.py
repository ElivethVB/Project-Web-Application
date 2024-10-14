import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar el conjunto de datos del Titanic
# Asegúrate de que el archivo CSV esté en la misma carpeta
df = pd.read_csv('titanic.csv')

# Encabezado
st.header("Análisis Exploratorio del Titanic")

# Casillas de verificación para seleccionar gráficos
histogram_checkbox = st.checkbox("Mostrar Histograma")
scatter_checkbox = st.checkbox("Mostrar Diagrama de Dispersión")

# Generar histograma si se selecciona la casilla
if histogram_checkbox:
    st.write("Histograma de Supervivencia")
    fig_histogram = px.histogram(df, x='Survived', title='Supervivencia en el Titanic',
                                 labels={'Survived': 'Supervivencia'},
                                 color='Survived',
                                 color_discrete_sequence=px.colors.qualitative.Pastel)
    st.plotly_chart(fig_histogram)

# Generar gráfico de dispersión si se selecciona la casilla
if scatter_checkbox:
    st.write("Diagrama de Dispersión de Edad vs. Tarifa")
    fig_scatter = px.scatter(df, x='Age', y='Fare', color='Survived',
                             title='Edad vs. Tarifa según Supervivencia',
                             labels={'Age': 'Edad', 'Fare': 'Tarifa'},
                             color_discrete_sequence=px.colors.qualitative.Pastel)
    st.plotly_chart(fig_scatter)
