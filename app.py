import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar el conjunto de datos del Titanic
# Asegúrate de que el archivo CSV esté en la misma carpeta
df = pd.read_csv('titanic.csv')

# Encabezado de la aplicación
st.header("Titanic Data Explorer")

# 1. Visualizador de Datos
st.subheader("Visualizador de Datos")
st.write("Aquí puedes ver las primeras filas del conjunto de datos del Titanic.")
st.dataframe(df.head())

# 2. Tipos de Pasajeros
st.subheader("Tipos de Pasajeros")
st.write("Este gráfico muestra la distribución de los pasajeros según su clase.")
fig_types = px.histogram(df, x='Pclass', title='Distribución de Pasajeros por Clase',
                         labels={'Pclass': 'Clase'},
                         color='Pclass',
                         color_discrete_sequence=px.colors.qualitative.Pastel)
st.plotly_chart(fig_types)

# 3. Histograma de Comparación
st.subheader("Histograma de Comparación de Supervivencia por Sexo")
fig_comparison = px.histogram(df, x='Sex', color='Survived', title='Comparación de Supervivencia por Sexo',
                              labels={'Sex': 'Sexo',
                                      'Survived': 'Supervivencia'},
                              color_discrete_sequence=px.colors.qualitative.Pastel)
st.plotly_chart(fig_comparison)

# 4. Comparación de Precios de Pasajes
st.subheader("Comparación de Precios de Pasajes por Clase")
st.write("Selecciona una clase para comparar los precios de los pasajes.")
class_options = df['Pclass'].unique()
selected_class = st.selectbox("Selecciona una Clase", class_options)

# Filtrar datos según la clase seleccionada
filtered_data = df[df['Pclass'] == selected_class]

if not filtered_data.empty:
    fig_price_comparison = px.box(filtered_data, x='Pclass', y='Fare', title=f'Comparación de Precios de Pasajes en Clase {selected_class}',
                                  labels={'Fare': 'Tarifa'},
                                  color='Pclass')
    st.plotly_chart(fig_price_comparison)
else:
    st.write("No hay datos disponibles para la clase seleccionada.")
