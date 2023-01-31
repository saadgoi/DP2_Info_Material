# Estructura visual

# Proceso ETL

Antes de emepzar con todo, lógicamente es necesario crear un proyecto sobre el cual trabajar. Para ello, vamos a la página del selector de proyectos de Google Cloud Console y creamos un proyecto de Google Cloud o seleccionamos uno si ya teníamos uno creado previamente.
</br></br>
Primero, crea un bucket de Cloud Storage mediante la consola de Google Cloud o Google Cloud CLI. La canalización de Dataflow usa este bucket como ubicación de almacenamiento temporal.
</br></br>
Los **buckets** son "contenedores" donde se almacenan los datos de forma temporal.

Para crear un bucket usaremos el siguiente código en la terminal de GCP
```
gsutil mb gs://BUCKET_NAME
```


Para crear un topic, usamos el comando:

```
gcloud pubsub topics create $TOPIC_ID
```

Y para una suscripción al dicho topic (para suscribirse a otros topics simplemente cambiar el TOPIC_ID):

```
gcloud pubsub subscriptions create --topic TOPIC_ID SUBSCRIPTION_ID
```
Otra herramienta útil en este proceso ETL que estamos realizando es el **cloud scheduler**. Un servicio que permite automatizar y evitar trabajo manual (entre ellos, automatizar la publicación de datos), por lo que podríamos usar esto para la publicación periódica de datos.
```
gcloud scheduler jobs create pubsub publisher-job --schedule="* * * * *" \
    --topic=$TOPIC_ID --message-body="Hello!"
```

# Ejecución

Cuando tengamos todo listo, simplemente ejecutaríamos el "Cloud Scheduler Job" para correr el pipeline.

```
gcloud dataflow jobs run JOB_NAME \
    --gcs-location gs://dataflow-templates/latest/PubSub_to_BigQuery \
    --region DATAFLOW_REGION \
    --staging-location gs://BUCKET_NAME/temp \
    --parameters \
inputTopic=projects/PROJECT_ID/topics/TOPIC_ID,\
outputTableSpec=PROJECT_ID:DATASET.TABLE_NAME


    --staging-location TEMP_LOCATION \
outputDeadletterTable=PROJECT_ID:DATASET.TABLE_NAME
```

# Ver los resultados escritos en Big Query

Para ver los datos simplemente tendríamos que ir a la consola de Big Query y realizar una consulta como por ejemplo:
</br></br>
*Habría que cambiar la información dentro de la query por la de nuestro proyecto*
```
SELECT * FROM `PROJECT_ID.tutorial_dataset.tutorial`
LIMIT 1000
```
# Limpieza final
