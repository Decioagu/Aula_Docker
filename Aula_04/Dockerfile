# Imagem base Python 3.11
FROM python:3.11-slim

# Instala SQLite
RUN apt-get update && apt-get install -y sqlite3 && rm -rf /var/lib/apt/lists/*

# Define diretório de trabalho
WORKDIR /app

# Copia o script Python para o container
COPY app.py .

# Comando para rodar o script
CMD ["python", "app.py"]
