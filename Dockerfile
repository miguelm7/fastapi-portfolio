# Usar una imagen base de Python con FastAPI
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar los archivos de la aplicación a /app
COPY . /app

# Instalar las dependencias si las hubiera (actualizar si hay un archivo requirements.txt)
RUN pip install --no-cache-dir -r requirements.txt

# Comando para correr la aplicación
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8001"]
