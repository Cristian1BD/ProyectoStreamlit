import streamlit as st
import pandas as pd
import os

st.title("📋 Registro de Estudiantes y Salidas Pedagógicas")

def cargar_datos(archivo):
    if os.path.exists(archivo):
        return pd.read_csv(archivo)
    else:
        return pd.DataFrame()

estudiantes = cargar_datos("estudiantes.csv")
salidas = cargar_datos("salidas.csv")

st.header("👨‍🎓 Registrar nuevo estudiante")
with st.form("form_estudiante"):
    documento = st.text_input("Documento")
    nombre = st.text_input("Nombre")
    grupo = st.text_input("Grupo")
    profesor = st.text_input("Profesor")
    enviar = st.form_submit_button("Guardar estudiante")

    if enviar:
        if documento and nombre and grupo and profesor:
            nuevo = pd.DataFrame([{
                "documento": documento,
                "nombre": nombre,
                "grupo": grupo,
                "profesor": profesor
            }])
            estudiantes = pd.concat([estudiantes, nuevo], ignore_index=True)
            estudiantes.to_csv("estudiantes.csv", index=False)
            estudiantes = pd.read_csv("estudiantes.csv")  # Recargar
            st.success("✅ Estudiante guardado correctamente")
        else:
            st.warning("⚠️ Por favor, completa todos los campos.")

st.divider()

st.header("🚌 Registrar salida pedagógica")
with st.form("form_salida"):
    doc_salida = st.text_input("Documento del estudiante")
    if doc_salida:
        estudiante = estudiantes[estudiantes["documento"].astype(str) == str(doc_salida)]
        if not estudiante.empty:
            st.info(f"Estudiante: {estudiante.iloc[0]['nombre']}")
        else:
            st.warning("⚠️ Documento no encontrado en la base de estudiantes.")

    destino = st.text_input("Destino")
    fecha = st.date_input("Fecha de salida")
    guardar = st.form_submit_button("Registrar salida")

    if guardar:
        if doc_salida and destino:
            nueva_salida = pd.DataFrame([{
                "documento": doc_salida,
                "destino": destino,
                "fecha": fecha
            }])
            salidas = pd.concat([salidas, nueva_salida], ignore_index=True)
            salidas.to_csv("salidas.csv", index=False)
            st.success("✅ Salida registrada correctamente")
        else:
            st.warning("⚠️ Completa todos los campos de la salida.")
