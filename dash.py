import streamlit as st
import pandas as pd
import plotly.express as px

# ---- Configuración de la Página ----
st.set_page_config(page_title="🌍 Dashboard Interactivo", layout="wide")

# ---- Cargar Datos ----
df = px.data.gapminder()

# ---- Título del Dashboard ----
st.title("🌍 Dashboard Interactivo con Streamlit y Plotly")

# ---- Sidebar con Filtros ----
st.sidebar.header("📊 Filtros")

# Selector de Continente
continent = st.sidebar.selectbox("🌎 Selecciona un Continente:", df["continent"].unique())

# Selector de Año
year = st.sidebar.slider("📅 Selecciona un Año:", int(df["year"].min()), int(df["year"].max()), int(df["year"].max()))

# Filtrar datos por año y continente seleccionado
filtered_df = df[(df["continent"] == continent) & (df["year"] == year)]

# ---- Métricas Claves en 2 Columnas ----
col1, col2 = st.columns(2)

with col1:
    # Centrar el valor de PIB Promedio
    st.markdown(f"""
    <div style="text-align: center; font-size: 16px;">
        <strong>📈 PIB Promedio:</strong> <br>
        <span style="font-size: 14px;">${filtered_df['gdpPercap'].mean():,.2f}</span>
    </div>
    """, unsafe_allow_html=True)

with col2:
    # Centrar el valor de Esperanza de Vida Promedio
    st.markdown(f"""
    <div style="text-align: center; font-size: 16px;">
        <strong>❤️ Esperanza de Vida Promedio:</strong> <br>
        <span style="font-size: 14px;">{filtered_df['lifeExp'].mean():.2f} años</span>
    </div>
    """, unsafe_allow_html=True)

# ---- Mostrar los gráficos en 2 columnas ----
col3, col4 = st.columns(2)

with col3:
    # Título centrado para el primer gráfico
    st.markdown(f"<h6 style='text-align: center;'>📌 PIB vs Esperanza de Vida en {continent} - Año {year}</h6>", unsafe_allow_html=True)
    fig1 = px.scatter(filtered_df, x="gdpPercap", y="lifeExp", 
                      size="pop", color="country", hover_name="country", log_x=True)
    st.plotly_chart(fig1, use_container_width=True)

with col4:
    # Título centrado para el gráfico de barras
    st.markdown(f"<h6 style='text-align: center;'>📌 Promedio de Esperanza de Vida por País en {continent} - Año {year}</h6>", unsafe_allow_html=True)
    # Cambiar histograma por un gráfico de barras
    bar_fig = px.bar(filtered_df, x="country", y="lifeExp", 
                     color="country", labels={"lifeExp": "Esperanza de Vida"})
    st.plotly_chart(bar_fig, use_container_width=True)

# ---- Comparación entre Continentes en Otra Fila ----
st.sidebar.subheader("📌 Comparación entre Continentes")
continent2 = st.sidebar.selectbox("🌍 Selecciona otro Continente para Comparar:", df["continent"].unique())

if continent != continent2:
    st.markdown(f"<h6 style='text-align: center;'>📊 Comparación entre {continent} y {continent2} - Año {year}</h6>", unsafe_allow_html=True)
    filtered_df2 = df[(df["continent"].isin([continent, continent2])) & (df["year"] == year)]
    
    fig3 = px.scatter(filtered_df2, x="gdpPercap", y="lifeExp", 
                      size="pop", color="continent", hover_name="country", log_x=True)
    st.plotly_chart(fig3, use_container_width=True)

# ---- Mensaje Final ----
st.info("📌 Usa los filtros en la barra lateral para explorar los datos 📊")

