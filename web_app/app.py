import requests
from bs4 import BeautifulSoup
import pymongo
from flask import Flask, render_template, request

app = Flask(__name__)

# Configuración de la base de datos MongoDB
client = pymongo.MongoClient("mongodb://mongo:27017/")
db = client["web_scraping_db"]
results_collection = db["results"]

# Cargar las palabras comunes desde el archivo common.txt
with open("wordlists/common.txt", "r") as f:
    common_words = set(f.read().splitlines())

def discover_routes(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            links = soup.find_all('a')
            routes = [link.get('href') for link in links if link.get('href') and any(word in link.get('href') for word in common_words)]
            return routes
        else:
            print("La petición a la URL no fue exitosa.")
            return []
    except Exception as e:
        print("Error al obtener las rutas:", e)
        return []

def save_to_database(url, routes):
    # Insertar solo las rutas que coincidan con las palabras comunes en la base de datos
    common_routes = [route for route in routes if any(word in route for word in common_words)]
    results_collection.insert_one({'url': url, 'routes': common_routes})
    print("Resultados insertados en la base de datos.")

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'descubrir_rutas' in request.form:
            url = request.form.get('url')
            if not url:
                return render_template('index.html', error='Por favor, introduzca una URL válida.')

            # Llama a la función para descubrir rutas
            discovered_routes = discover_routes(url)
            print("Rutas descubiertas:", discovered_routes)

            # Guarda los resultados en la base de datos
            save_to_database(url, discovered_routes)

        elif 'vaciar_rutas' in request.form:
            # Eliminar todas las entradas en la colección de resultados
            results_collection.delete_many({})
            print("Se han eliminado todas las rutas descubiertas.")

    # Obtener todos los resultados de la base de datos
    all_results = results_collection.find()

    return render_template('index.html', results=all_results)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
