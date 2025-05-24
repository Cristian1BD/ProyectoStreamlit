import pandas as pd

# Lista de datos simulados
data = [
    {"documento": 123456, "nombre": "Ana Torres", "grupo": "6A", "profesor": "Profe Juan"},
    {"documento": 234567, "nombre": "José Martínez", "grupo": "6A", "profesor": "Profe Juan"},
    {"documento": 345678, "nombre": "Luis García", "grupo": "6B", "profesor": "Profe Laura"},
    {"documento": 456789, "nombre": "María López", "grupo": "6C", "profesor": "Profe Juan"},
    {"documento": 567890, "nombre": "Carlos Ruiz", "grupo": "6B", "profesor": "Profe Laura"},
]

# Convertir a DataFrame
df = pd.DataFrame(data)

# Guardar como CSV
df.to_csv("estudiantes.csv", index=False)

print("✅ Archivo 'estudiantes.csv' creado correctamente.")
