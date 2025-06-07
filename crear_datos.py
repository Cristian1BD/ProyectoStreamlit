import pandas as pd
from faker import Faker
import random

fake = Faker('es_MX')
Faker.seed(123)

grupos = ['6A', '6B', '6C', '7A', '7B', '7C']
profesores = ['Profe Juan', 'Profe Laura', 'Profe Carlos', 'Profe Ana']

data = []
for i in range(5000):
    data.append({
        "documento": fake.unique.random_int(min=100000, max=999999),
        "nombre": fake.name(),
        "grupo": random.choice(grupos),
        "profesor": random.choice(profesores)
    })

df = pd.DataFrame(data)
df.to_csv("estudiantes.csv", index=False)
print("✅ Archivo 'estudiantes.csv' con 5000 registros creado correctamente.")
