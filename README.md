# mongo_route_extractor

Creamos dos servicios orquestados:
1.  Base de Datos de Mongo con dos tablas:

-	Una tabla con un diccionario (common.txt)
-	Una tabla con resultados (base de datos de mongo db)

2. Una web con Python, Flask donde se mete la dirección de una web (la que sea) y tiene que hacer un Discovery de todas las posibles rutas de esa web. Estos resultados se deben mostrar en la otra parte y se deben extraer usando el diccionario.

### Creamos los siguientes codigos:

Carpeta de **mongo**:
 - Un **Dockerfile** para la  base de datos de Mongo
 - El **init-db.js** que explica como crear la colección para almacenar los resultados

Carpeta de **web_app**:
 - Carpeta de **templates** con el **index.html** del buscador
 - Carpeta de **wordlist** con el **common.txt** con un diccionario de rutas
 - El **app.py** con toda la logica de la extraccion y almacenamiento de las rutas
 - Un **Dockerfile** para la pagina web
 - Un **requirements.txt** con los requisitos necesarios

Un **docker-compose.yml** para coordinar ambos servicios dentro del contendor de Docker

### Para probarlo realizamos los siguientes pasos:

1. Accedemos a la Windods PowerShell.
2. Accedemos a donde este nuestra carpeta con los anteriores contenidos, usando el comando **C:\Users\hecto\pruebas_docker\Docker-Compose**
3. Creamos el contenedor con el comando **docker-compose up --build**

   ![image](https://github.com/HectorCRZBQ/mongo_route_extractor/assets/148070442/000b6e25-74d6-47aa-909f-2aa252b4511f)

4. Para verlo en el buscador acedemos por medio del enlace: **http://localhost:5000**

![image](https://github.com/HectorCRZBQ/mongo_route_extractor/assets/148070442/cd12a093-55d3-4792-832f-044d64725e43)
