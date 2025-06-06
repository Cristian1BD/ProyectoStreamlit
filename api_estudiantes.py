from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

app = FastAPI()

# CORS para permitir acceso desde Streamlit
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/resumen")
def resumen_estudiantes():
    df = pd.read_csv("estudiantes.csv")
    resumen = {
        "total_estudiantes": len(df),
        "grupos": df['grupo'].value_counts().to_dict(),
        "profesores": df['profesor'].value_counts().to_dict()
    }
    return resumen
