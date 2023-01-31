import pandas as pd
import uuid
import time

# Crear dataframe y eliminar columnas innecesarias
df = pd.read_csv("MOCK.csv")
#print(df)

# Guardar datos necesarias iterando por cada fila en un JSON
def iterate_rows():
    for index, row in df.iterrows():
        sensor_data = {"id": uuid.uuid1(), 
                        "time": row["first_name"],
                        "pressure": row["email"]}
        time.sleep(2)
        #print(sensor_data)
    return sensor_data

# Tener una API indefinida
while True:
    iterate_rows()
# Ejecutar la función en un bucle indefinido para fingir una API

