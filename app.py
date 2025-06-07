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

# Cargar variables de entorno
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Cliente de OpenAI
client = OpenAI(api_key=api_key)

# Configuración de la página
st.set_page_config(page_title="Filtro de Estudiantes", layout="wide")
st.title("🎒 Filtro de Estudiantes - Salidas Pedagógicas")

# Función para cargar datos
@st.cache_data
def cargar_datos():
    return pd.read_csv("estudiantes.csv")

df = cargar_datos()

# Tabs
tab1, tab2, tab3, tab4 = st.tabs(["📋 Filtros", "📊 Análisis Exploratorio", "🧠 Consulta con IA", "📡 Resumen API"])

# ----------------------- TAB 1: FILTROS -----------------------
with tab1:
    st.subheader("👨‍🎓 Lista completa")
    st.dataframe(df)

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

    st.subheader("📋 Resultados filtrados")
    st.dataframe(filtro)

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

# ----------------------- TAB 2: EDA -----------------------
with tab2:
    st.subheader("📊 Distribución por grupo")
    total_estudiantes_grupo = len(df)
    fig_grupo = px.histogram(df, x="grupo", color="grupo", title="Estudiantes por Grupo")
    fig_grupo.add_annotation(
        text=f"Total estudiantes: {total_estudiantes_grupo}",
        xref="paper", yref="paper",
        x=0.5, y=1.15,  # Centrado arriba
        showarrow=False,
        font=dict(size=16, color="black")
    )
    st.plotly_chart(fig_grupo, use_container_width=True)

    st.subheader("📊 Distribución por profesor")
    total_estudiantes_profesor = len(df)
    fig_profesor = px.histogram(df, x="profesor", color="profesor", title="Cantidad de estudiantes por profesor")
    fig_profesor.add_annotation(
        text=f"Total estudiantes: {total_estudiantes_profesor}",
        xref="paper", yref="paper",
        x=0.5, y=1.15,
        showarrow=False,
        font=dict(size=16, color="black")
    )
    st.plotly_chart(fig_profesor, use_container_width=True)

    st.subheader("🏆 Top 5 profesores con más estudiantes")
    top_profesores = df['profesor'].value_counts().nlargest(5).reset_index()
    top_profesores.columns = ["Profesor", "Cantidad"]
    st.dataframe(top_profesores)

# ----------------------- TAB 3: IA -----------------------
with tab3:
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

# ----------------------- TAB 4: API -----------------------
with tab4:
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
