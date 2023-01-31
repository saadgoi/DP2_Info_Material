Antes de emepzar con todo, es necesario crear un proyecto sobre el cual trabajar. Para ello, vamos a la página del selector de proyectos de Google Cloud Console y creamos un proyecto de Google Cloud o seleccionamos uno si ya teníamos uno creado previamente.
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
