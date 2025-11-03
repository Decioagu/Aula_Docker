### Aula_01
### 1º - Crie seu programa PYTHON

- Arquivo: 
````
calculo_imc.py
````
---

### 2º - Criar o Dockerfile
No seu projeto, crie um arquivo chamado Dockerfile (sem extensão). Exemplo simples com Python:

- Definições:
    - FROM → Define a imagem base (ex: um Linux com Python, Node, etc.).
    - LABEL → Serve para adicionar metadados à imagem Docker, informações extras na imagem.
    - WORKDIR → Cria e define o diretório de trabalho dentro do container para execução do programa.
    - COPY / ADD → Copia arquivos do seu PC para dentro da imagem.
    - RUN → Executa comandos na construção da imagem (instalação de pacotes).
    - EXPOSE → Serve para documentar quais portas a aplicação dentro do container vai escutar.
    - ENV → Serve para definir variáveis de ambiente dentro da imagem/container.
    - EXPOSE → Documenta a porta que o container vai expor.
    - CMD → Define o comando padrão que o container vai rodar.
    - ENTRYPOINT → Define o programa principal que será executado sempre que o container iniciar.

<br>

- Com o Docker Desktop aberto
````
FROM python:3.12-slim
LABEL maintainer="Decio <decio@email.com>"
LABEL version="1.0"
LABEL description="Imagem para calcular IMC com Python"
WORKDIR /app/
COPY calculo_imc.py /app
CMD ["python", "calculo_imc.py"] 
````
<br>

- Observações: 
    - "FROM python:3.12-slim" não depende da versão do Python que você tem instalada no seu computador local. Isso porque o FROM pega uma imagem oficial do Python no Docker Hub, que já vem com o Python dentro do contêiner.
    - O Docker Hub é um serviço em nuvem oficial da Docker que funciona como um repositório central de imagens Docker. 
    - Em "WORKDIR /app" o "/app" define o diretório de trabalho dentro do container
    - Use "COPY" para copiar arquivos dentro da imagem (DockerFile)
    - Use "ADD" para copiar arquivos dentro da imagem, mas com recursos extras como: baixar da internet ou extrair .tar.
    - CMD e ENTRYPOINT são semelhante ao iniciar container, porem possui propriedades distintas.
---


### 3º - Criar a imagem
No PowerShell ou Prompt de Comando, navegue até a pasta do projeto (onde está o Dockerfile):

````
cd C:\caminho\do\projeto
docker build -t __NOME DA IMAGEM__ -f __NOME DO ARQUIVO DOCKERFILE PERSONALIZADO__ .
````
- Definições:
    - docker build = cria imagem a partir do Dockerfile:
        - -t = nome/tag da imagem.
        - -f = especificar Dockerfile.
        - --build-arg = passar variáveis para o build.
        - --no-cache = não usar cache.
        - --pull = atualizar base.
        - --target = multi-stage.
        - --platform = escolher arquitetura.
        - . = usar pasta atual.



- Com o Docker Desktop aberto
````
cd C:\REPOSITORIO\Aula_Docker\Aula_01
docker build -t imagem_calculo_imc_aula_01 .
````
---

### 4º - Visualizar imagem ou ler arquivo Dockerfile

- Com o Docker Desktop aberto
````
- docker ps         → Listar todas as imagens em Docker Desktop em execução
- docker ps -a      → Listar todas as imagens existente em Docker Desktop
- docker ps -aq     → Listar todas os ID das imagens existente em Docker Desktop
- docker images     → Listar todas as imagens existente em Docker Desktop
- cat Dockerfile    → Ler arquivo Dockerfile da pasta atual
````
---- 

### 5º - Cria e iniciar um container a partir de uma imagem


````
docker run -it -- name __NOME DO CONTAINER__ __NOME DA IMAGEM__ 
````
- Definição de parâmetros:
    - --name → Nomear container
    - -d → Rodar em background
    - -p → Mapear portas
    - -v → Volumes/persistência
    - -e → Variáveis de ambiente
    - -it → Interativo/terminal
    - --rm → Remove ao parar
    - --network → Conecta a rede

<br>

- Com o Docker Desktop aberto:
````
docker images   → Lista de todas as imagens existente no Docker Desktop
docker run -it --name container_calculo_imc_aula_01 imagem_calculo_imc_aula_01
````
---

### 6º - Executar container
- Com o Docker Desktop aberto
````
docker start -ai container_calculo_imc_aula_01
docker exec container_calculo_imc_aula_01 bash
````
- Definições:
    - docker start → Só inicia o container, sem comandos novos.
    - docker exec → Só inicia o container, com outros comandos (ex: echo, bash, etc).

### 7º - Parar execução de imagem
Listar todos os containers (ativos e parados).
- Com o Docker Desktop aberto
````
docker images   → Lista de todas as imagens existente no Docker Desktop
docker ps       → Lista de imagem em execução
docker ps -a    → Lista de imagem já ativadas
````
Exemplo de lista: 
- CONTAINER ID   IMAGE                     COMMAND                  CREATED         
- 0746564a0197   imagem_calculo_imc_aula_01       "python calculo_imc.…"   8 minutes ago    

### 8º - Para execução de um container
- Com o Docker Desktop aberto
````
docker stop __ID OU NOME DO CONTAINER__
````
- Definições:
````
docker container prune  → Exclui container não usadas.
docker image prune      → Parar imagens não usadas.
docker volume prune     → Parar volumes não utilizados.
docker network prune    → Parar redes não usadas.
docker system prune     → Limpa tudo de uma vez (containers parados, imagens órfãs, redes não usadas,volumes anônimos).
````
---

### 9º - Excluir imagem

- Com o Docker Desktop aberto
````
docker rmi __ID OU NOME DA IMAGEM__     → Excluir imagem - NÃO pode estrar em execução
````
---

### 10º - Excluir container

- Com o Docker Desktop aberto
````
docker rm __ID OU NOME DO CONTAINER__     → Excluir container - NÃO pode estrar em execução
````

### 11º - Informações detalhadas da imagem em formato JSON

- Com o Docker Desktop aberto
````
docker inspect __ID__
docker inspect __NOME DO ARQUIVO__
````