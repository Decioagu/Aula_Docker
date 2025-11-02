# Usa a imagem base do Python
FROM python:3.12-slim

# Informações sobre a imagem Docker 
LABEL maintainer="Decio <decio@email.com>"
LABEL version="1.0"
LABEL description="Imagem para calcular IMC com Python"
LABEL nome_container="container_calculo_imc_aula_01"

# Cria o diretório de trabalho no container para executar o programa
WORKDIR /app 

# Copia o arquivo para o diretório de trabalho
COPY calculo_imc.py /app/

# Comando para executar o programa
CMD ["python", "calculo_imc.py"] 