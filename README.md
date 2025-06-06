# Proyecto Streamlit: Filtro de Estudiantes con Análisis, API e IA Generativa

## Descripción

Este proyecto es una aplicación web desarrollada con Streamlit que permite filtrar y analizar datos de estudiantes para salidas pedagógicas. Incluye:

- Carga y análisis interactivo de un dataset de estudiantes.
- Visualizaciones dinámicas con Plotly.
- Consumo de una API simulada para registrar y mostrar estudiantes.
- Integración con una API de IA generativa (OpenAI) para consultas inteligentes basadas en los datos.

## Estructura del Proyecto

- `app.py`: Archivo principal con la interfaz Streamlit, filtros, gráficos y conexión con API e IA.
- `generar_datos.py`: Script para generar un CSV con datos simulados de estudiantes.
- `.env`: Archivo para almacenar la clave de la API OpenAI (no incluido en el repositorio).
- `requirements.txt`: Dependencias del proyecto.
- `.gitignore`: Archivos y carpetas ignoradas por Git.

## Cómo Ejecutar

1. Clona el repositorio:
   ```bash
   git clone <url-del-repo>
   cd <nombre-del-proyecto>
2. Crea y activa un entorno virtual:
python -m venv venv
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate     # Windows
3. Instala las dependencias:
pip install -r requirements.txt
4. OPENAI_API_KEY=tu_clave_aqui
5.streamlit run app.py
Funcionalidades
Visualización y filtrado de estudiantes por documento, grupo y profesor.

Gráficos interactivos de distribución por grupo.

Exportación de resultados filtrados a Excel.

Registro y consulta de estudiantes mediante API simulada.

Consulta generativa con IA para análisis y generación de texto basado en datos.

Tecnologías y Librerías
Python 3.x

Streamlit

Pandas

Plotly

OpenAI API

python-dotenv

Notas
La clave API de OpenAI debe estar configurada en .env para habilitar la función de IA generativa.

El proyecto incluye manejo básico de errores para consultas a la API de OpenAI.

Puedes ampliar el proyecto agregando APIs reales o modelos de IA adicionales.
