import streamlit as st
import pandas as pd
import plotly.express as px
import requests
from io import BytesIO
import base64
import openai
from openai import OpenAI
from dotenv import load_dotenv
import os

# Configuración de la página
st.set_page_config(page_title="Filtro de Estudiantes", layout="wide")
st.title("🎒 Filtro de Estudiantes - Salidas Pedagógicas")

# Función para cargar datos del CSV
def cargar_datos():
    return pd.read_csv("estudiantes.csv")

df = cargar_datos()

# 🔹 Sección 1: Visualización general
st.subheader("👨‍🎓 Lista completa")
st.dataframe(df)

# 🔹 Sección 2: Filtros interactivos
st.sidebar.header("🔎 Filtros")
documento = st.sidebar.text_input("Buscar por Documento")
grupo = st.sidebar.selectbox("Grupo", options=["Todos"] + sorted(df['grupo'].unique()))
profesor = st.sidebar.selectbox("Profesor", options=["Todos"] + sorted(df['profesor'].unique()))

filtro = df.copy()
if documento:
    filtro = filtro[filtro['documento'].astype(str).str.contains(documento)]
if grupo != "Todos":
    filtro = filtro[filtro['grupo'] == grupo]
if profesor != "Todos":
    filtro = filtro[filtro['profesor'] == profesor]

# 🔹 Sección 3: Resultados filtrados
st.subheader("📋 Resultados filtrados")
st.dataframe(filtro)

# 🔹 Sección 4: Gráfico por grupo
st.subheader("📊 Distribución por grupo")
grupo_fig = px.histogram(filtro, x="grupo", color="grupo", title="Estudiantes por Grupo")
st.plotly_chart(grupo_fig, use_container_width=True)

# 🔹 Sección 5: Exportar a Excel
def exportar_excel(dataframe):
    output = BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        dataframe.to_excel(writer, index=False, sheet_name='Estudiantes')
    return output.getvalue()

st.subheader("⬇️ Exportar resultados")
if not filtro.empty:
    excel_bytes = exportar_excel(filtro)
    b64 = base64.b64encode(excel_bytes).decode()
    href = f'<a href="data:application/octet-stream;base64,{b64}" download="estudiantes_filtrados.xlsx">📥 Descargar Excel</a>'
    st.markdown(href, unsafe_allow_html=True)
else:
    st.info("No hay datos para exportar.")

# 🔹 Sección 6: Consumo de API simulada
st.subheader("📡 Resumen desde API Local")

if st.button("Consultar resumen"):
    try:
        response = requests.get("http://127.0.0.1:8000/api/resumen")
        if response.status_code == 200:
            data = response.json()
            st.success(f"Total estudiantes: {data['total_estudiantes']}")
            st.write("👥 Estudiantes por grupo:")
            st.json(data['grupos'])
            st.write("👨‍🏫 Estudiantes por profesor:")
            st.json(data['profesores'])
        else:
            st.error("Error al consultar la API.")
    except Exception as e:
        st.error(f"Error: {e}")
# Cargar clave desde archivo .env
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Crear cliente moderno
client = OpenAI(api_key=api_key)

st.subheader("🧠 Consulta con IA Generativa")

prompt = st.text_area("Escribe una consulta sobre los estudiantes (ej. resumen, análisis, etc.):")

if st.button("Consultar IA"):
    if prompt:
        with st.spinner("Generando respuesta..."):
            try:
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "Eres un asistente que analiza datos de estudiantes."},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.7,
                    max_tokens=300
                )
                st.success("Respuesta generada:")
                st.write(response.choices[0].message.content)
            except Exception as e:
                st.error(f"Error al consultar la IA: {str(e)}")
    else:
        st.warning("Por favor escribe un prompt.")