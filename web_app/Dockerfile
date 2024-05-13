# Usa una imagen base de Python
FROM python:3.8-slim

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el archivo de requisitos (requirements.txt) para instalar dependencias de Python
COPY requirements.txt requirements.txt

# Instala las dependencias necesarias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia el contenido de la aplicación en el contenedor
COPY . .

# Exponer el puerto en el que Flask está ejecutando la aplicación
EXPOSE 5000

# Comando para iniciar la aplicación Flask
CMD ["python", "app.py"]
