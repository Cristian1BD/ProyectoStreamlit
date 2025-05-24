import streamlit as st
import pandas as pd
import plotly.express as px
from io import BytesIO
import base64

st.set_page_config(page_title="Filtro de Estudiantes", layout="wide")
st.title("🎒 Filtro de Estudiantes - Salidas Pedagógicas")

def cargar_datos():
    return pd.read_csv("estudiantes.csv")

df = cargar_datos()

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

st.subheader("📊 Distribución por grupo")
grupo_fig = px.histogram(filtro, x="grupo", color="grupo", title="Estudiantes por Grupo")
st.plotly_chart(grupo_fig, use_container_width=True)

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
