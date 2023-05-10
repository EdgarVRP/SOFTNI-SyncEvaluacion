# SOFTNI_SyncEvaluacion

Instrucciones:

pip install Flask

pip install Flask-RESTful

pip install pymongo

pip install python-dotenv

para correr el servicio flask run

Se instala flask-cors para permitir solicitudes agenas al servidor backend

pip install flask-cors

Se instala el paquete python-dotenv para manejar las variables de entorno

pip install python-dotenv

Para el despliegue en railway es necesario:

Se crea el archivo `Procfile` en la raiz con lo siguiente:

web: gunicorn app:app

Se instala la herramienta:

pip install pipreqs

Se el siguientecodigo para generar el requirements.txt:

pipreqs .
