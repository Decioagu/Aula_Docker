# Usar Python oficial
FROM python:3.11-slim

# Definir diretório de trabalho
WORKDIR /app

# Copiar arquivos
COPY requirements.txt .
COPY app.py .

# Instalar dependências
RUN pip install --no-cache-dir -r requirements.txt

# Comando padrão
CMD ["python", "app.py"]
