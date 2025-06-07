from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

app = FastAPI()

# Permitir peticiones desde cualquier origen (útil para Streamlit local)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/resumen")
def resumen_estudiantes():
    try:
        df = pd.read_csv("estudiantes.csv")
        resumen = {
            "total_estudiantes": len(df),
            "grupos": df['grupo'].value_counts().to_dict(),
            "profesores": df['profesor'].value_counts().to_dict()
        }
        return resumen
    except Exception as e:
        return {"error": str(e)}
