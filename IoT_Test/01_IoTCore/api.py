import pandas as pd
import uuid
import time
import json

# Crear dataframe y eliminar columnas innecesarias
df = pd.read_csv("dataset.csv")
#print(df)

def iterate_rows():
    # Tener una API indefinida
    while True:
        #iterando por cada fila del dataframe
        for index, row in df.iterrows():
            # guardar datos necesarios en una variable del formato json
            sensor_data = {"id": str(uuid.uuid1()), 
                            "time": row["FECHA"],
                            "pressure": row["SP Presión absoluta mb"], 
                            "temperature": row["SP Tª masa SW"]}
            # guardar la variable en un archivo json, que se sobreescribe cada segundo 
            with open("sensor_data.json", "w") as jsonFile:
                json.dump(sensor_data, jsonFile)
            time.sleep(1)
            #print(sensor_data)
        return sensor_data

iterate_rows()

