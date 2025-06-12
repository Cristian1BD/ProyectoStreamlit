# 🎒 Proyecto Streamlit: Filtro de Estudiantes con Análisis, API e IA Generativa

## 📌 Descripción

Aplicación web desarrollada con **Streamlit** que permite:

- Filtrar estudiantes por documento, grupo o profesor.
- Analizar datos con visualizaciones interactivas usando **Plotly**.
- Exportar resultados filtrados a Excel.
- Consultar datos desde una API local (**FastAPI** + **Uvicorn**).
- Realizar análisis automáticos con **IA generativa de OpenAI**.

✅ También está desplegado en Streamlit Community Cloud para acceso público sin necesidad de instalación local.

---

## 🗂️ Estructura del Proyecto

```
PROYECTOSTREAMLIT/
│
├── .env                       # Clave OpenAI (no versionado)
├── .gitignore                 # Archivos ignorados (como .venv, __pycache__)
├── README.md                  # Este archivo
├── requirements.txt           # Dependencias con versiones específicas
│
├── app.py                     # App principal Streamlit
├── generar_datos.py           # Script para generar el CSV de estudiantes
├── crear_datos.py             # Script auxiliar
├── api_estudiantes.py         # API local (FastAPI)
│
├── estudiantes.csv            # Dataset principal
├── salidas.csv                # Dataset adicional
│
├── pages/
│   └── 1_📋_Registro.py       # Página con formulario en Streamlit
│
└── .venv/                     # Entorno virtual (no se incluye en Git)
```

---

## ⚙️ Instalación y Ejecución

### 1. Clona el repositorio
```bash
git clone <URL-del-repo>
cd PROYECTOSTREAMLIT
```

### 2. Crea y activa el entorno virtual
```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# Linux / Mac
source .venv/bin/activate
```

### 3. Instala las dependencias
```bash
pip install -r requirements.txt
```

### 4. Configura tu clave OpenAI
Crea un archivo `.env` en la raíz del proyecto con el siguiente contenido:
```env
OPENAI_API_KEY=tu_clave_de_openai
```

### 5. Ejecuta la API local (en una terminal separada)
```bash
uvicorn api_estudiantes:app --reload
```

### 6. Ejecuta la aplicación Streamlit
```bash
streamlit run app.py
```

---

## 🎯 Funcionalidades

- ✅ **Filtros dinámicos** por documento, grupo y profesor.
- ✅ **Visualización interactiva** con Plotly.
- ✅ **Exportación a Excel** (XlsxWriter).
- ✅ **Consulta IA (OpenAI)** para análisis o resúmenes automáticos.
- ✅ **Consumo de API local** (FastAPI) para estadísticas resumidas.
- ✅ **Manejo de errores** para APIs.

---

## 🧪 Requisitos Técnicos

### Versión de Python recomendada:
```text
Python 3.10 o superior
```

### Librerías principales usadas:
- `streamlit==1.45.1`
- `pandas==2.3.0`
- `plotly==6.1.2`
- `openai==1.84.0`
- `fastapi==0.115.12`
- `uvicorn==0.34.3`
- `python-dotenv==1.1.0`
- `XlsxWriter==3.2.3`

Ver lista completa en [`requirements.txt`](./requirements.txt)

---

## 📝 Notas Finales

- No olvides activar el entorno virtual antes de ejecutar la app.
- Si no configuras correctamente la clave `.env`, la función de IA no funcionará.
- Puedes extender el proyecto con base de datos, autenticación de usuarios, roles, etc.