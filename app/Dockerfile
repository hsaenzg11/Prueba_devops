# Usa la imagen de Python como base
FROM python:3.9

# Copia el código de la aplicación al contenedor
COPY . /app 

# Establece el directorio de trabajo
WORKDIR /app

# Instala las dependencias
RUN pip3 install -r requirements.txt

# Expone el puerto 5000
EXPOSE 5000

# Define el comando de inicio
CMD ["python", "app.py"]

