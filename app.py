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
st.subheader("Distribución de Pasajeros por Clase")
if st.checkbox("Mostrar Distribución de Pasajeros"):
    fig_types = px.histogram(df, x='Pclass', title='Distribución de Pasajeros por Clase',
                             labels={'Pclass': 'Clase'},
                             color='Pclass',
                             color_discrete_sequence=px.colors.qualitative.Pastel)
    st.plotly_chart(fig_types)

# 3. Histograma de Comparación de Supervivencia
st.subheader("Comparación de Supervivencia por Sexo")
if st.checkbox("Mostrar Histograma de Supervivencia por Sexo"):
    fig_comparison = px.histogram(df, x='Sex', color='Survived', title='Comparación de Supervivencia por Sexo',
                                  labels={'Sex': 'Sexo',
                                          'Survived': 'Supervivencia'},
                                  color_discrete_sequence=px.colors.qualitative.Pastel)
    st.plotly_chart(fig_comparison)

# 4. Comparación de Tarifas
st.subheader("Comparación de Tarifas")
st.write("Selecciona una variable para comparar con las tarifas de los pasajes.")

# Opciones para comparar
comparison_options = ['Clase', 'Sexo', 'Edad']
comparison_variable = st.selectbox(
    "Selecciona la variable a comparar", comparison_options)

# Mostrar automáticamente la comparación de tarifas según la variable seleccionada
if comparison_variable == 'Clase':
    fig_price_comparison = px.box(df, x='Pclass', y='Fare', title='Comparación de Tarifas por Clase',
                                  labels={'Fare': 'Tarifa', 'Pclass': 'Clase'},
                                  color='Pclass')
    st.plotly_chart(fig_price_comparison)

elif comparison_variable == 'Sexo':
    fig_price_comparison = px.box(df, x='Sex', y='Fare', title='Comparación de Tarifas por Sexo',
                                  labels={'Fare': 'Tarifa', 'Sex': 'Sexo'},
                                  color='Sex')
    st.plotly_chart(fig_price_comparison)

elif comparison_variable == 'Edad':
    fig_price_comparison = px.scatter(df, x='Age', y='Fare', color='Survived',
                                      title='Comparación de Tarifas según Edad',
                                      labels={'Fare': 'Tarifa', 'Age': 'Edad'},
                                      color_continuous_scale=px.colors.sequential.Viridis)
    st.plotly_chart(fig_price_comparison)

# Gráfico de Supervivencia por Clase
st.subheader("Supervivencia por Clase")
if st.checkbox("Mostrar Gráfico de Supervivencia por Clase"):
    fig_survival_class = px.histogram(df, x='Pclass', color='Survived',
                                      title='Supervivencia por Clase',
                                      labels={'Pclass': 'Clase',
                                              'Survived': 'Supervivencia'},
                                      color_discrete_sequence=px.colors.qualitative.Pastel)
    st.plotly_chart(fig_survival_class)

# Gráfico de Distribución de Edades
st.subheader("Distribución de Edades de los Pasajeros")
if st.checkbox("Mostrar Gráfico de Distribución de Edades"):
    fig_age_distribution = px.histogram(df, x='Age', title='Distribución de Edades de los Pasajeros',
                                        labels={'Age': 'Edad'},
                                        color_discrete_sequence=px.colors.qualitative.Pastel)
    st.plotly_chart(fig_age_distribution)
