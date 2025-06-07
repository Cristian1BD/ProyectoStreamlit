# generar_datos.py
import pandas as pd
import random
from faker import Faker

fake = Faker('es_MX')  # Genera datos en español
Faker.seed(42)

grupos = [f"A{i}" for i in range(1, 11)]
profesores = [fake.name() for _ in range(10)]

data = []

for _ in range(5000):
    estudiante = {
        "documento": fake.unique.random_int(min=1000000000, max=9999999999),
        "nombre": fake.name(),
        "grupo": random.choice(grupos),
        "profesor": random.choice(profesores)
    }
    data.append(estudiante)

df = pd.DataFrame(data)
df.to_csv("estudiantes.csv", index=False)
print("✅ Archivo estudiantes.csv creado con 5000 registros.")
