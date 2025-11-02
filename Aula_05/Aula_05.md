### Aula_05
### Volumes MySQL

Criação de Volume com banco de dados MySQL.

**Criados Volume Docker:**

- docker volume create volume_mysql_aula_05

-----------------------------------------------------------------------------------------------------------

**Criar um Container MySQL no Volume Docker:** 

- docker run -d --name  __NOME DO CONTAINER MYSQL__ `
- -e MYSQL_ROOT_PASSWORD=__SENHA DO MYSQL WORKBENCH__ `
- -e MYSQL_DATABASE=__NOME DO BANCO MYSQL DOCKER__ `
- -e MYSQL_USER=__CRIA USUÁRIO DOCKER__ `
- -e MYSQL_PASSWORD=__SENHA USUÁRIO DOCKER__ `
- -v __NOME DO VOLUME__:/var/lib/mysql `
- -p 3307:3306 `
- mysql:8.0

O que cada parte faz:

- docker run → roda o Docker.
- -d → roda em segundo plano.
- --name __NOME DO CONTAINER MYSQL__ → nome do container dentro do Volume Docker.
- -e MYSQL_ROOT_PASSWORD=__SENHA DO MYSQL WORKBENCH__ → senha do usuário root MySQL.
- -e MYSQL_DATABASE=__NOME DO BANCO MYSQL DOCKER__ → cria um banco para o Volume do Docker.
- -e MYSQL_USER=__CRIA USUÁRIO DOCKER__ → cria um usuário para acesso Volume do Docker.
- -e MYSQL_PASSWORD=__SENHA USUÁRIO DOCKER__ → cria um senha para acesso Volume do Docker.
- -v __NOME DO VOLUME__:/var/lib/mysql → monta o volume no diretório de dados do MySQL.
- -p 3307:3306 → mapeando porta diferente da porta do MySQL localhost root
- mysql:8.0 → Nome da imagem usada para criar o contêiner (oficial do MySQL (versão 8.0) disponível no Docker Hub).

- Mapeando porta o que isso significa:
    - -p 3307:3306 → -porta host:container
        - 3306 → é a porta interna do container, ou seja, a porta que o MySQL está escutando dentro do container.
        - 3307 → é a porta externa do host, ou seja, a porta que você vai usar no seu computador (Windows, Linux, etc.) para se conectar ao MySQL que está dentro do container.
        - Mapeamento das portas (host:container): permite que uma porta do host “apontar” para uma porta específica do container.

Exemplo:

docker run -d `
--name container_mysql_aula_05 `
-e MYSQL_ROOT_PASSWORD=Enigma.2 `
-e MYSQL_DATABASE=banco_docker `
-e MYSQL_USER=decio `
-e MYSQL_PASSWORD=decio123 `
-v volume_mysql_aula_05:/var/lib/mysql `
-p 3307:3306 `
mysql:8.0

**Verificar o Volume:**
- docker volume ls
- docker volume inspect volume_mysql_aula_05

-----------------------------------------------------------------------------------------------------------

**ATIVAR CONTAINER MYSQL**

docker start container_mysql_aula_05

![alt text](DOCKER.png)

**DADOS CONTAINER MYSQL**

- docker run -d `
- --name container_mysql_aula_05 `
- -e MYSQL_ROOT_PASSWORD=Enigma.2 `
- -e MYSQL_DATABASE=banco_docker `
- -e MYSQL_USER=decio `
- -e MYSQL_PASSWORD=decio123 `
- -v volume_mysql_aula_05:/var/lib/mysql `
- -p 3307:3306 `
- mysql:8.0

![alt text](<DADOS CONTAINER MYSQL.png>)

**MYSQL WORKBENCH**

![alt text](WORKBENCH.png)

-----------------------------------------------------------------------------------------------------------

**Criar uma rede Docker:**
- docker network create rede_banco_mysql_aula_05

**Conectar container MySQL na rede criada:**
- docker network connect rede_banco_mysql_aula_05 container_mysql_aula_05

**Identificar conexão da rede ao container:**
- docker network inspect rede_banco_mysql_aula_05 (procurar por container)
- docker inspect container_mysql_aula_05 (procurar por rede)

- Comandos para rede:
    - docker network create __NOME DA REDE CONEXÃO__ → (__criar rede de conexão Docker__)
    - docker network ls → (__visualizar lista rede__)
    - docker network inspect __NOME DA REDE CONEXÃO__ → (__inspecionar rede__)
    - docker network disconnect __NOME DA REDE CONEXÃO__ __NOME DA IMAGEM__ → (__desconectar rede do container__)
    - docker network connect __NOME DA REDE CONEXÃO__ __NOME DA IMAGEM__ → (__conectar rede do container__)
    - docker network rm __NOME DA REDE CONEXÃO__ → (__excluir container rede__)

-----------------------------------------------------------------------------------------------------------

**Criar container para rede de conexão MySQL:**

cd C:\REPOSITORIO\Aula_Docker\Aula_05

Criar o programa Python (__app.py__)
- No arquivo Python é definido nome do banco de dados e a execução da linha de código

Criar o Dockerfile
- (Imagem) instala pacotes de acesso ao MySQL

Criar arquivo requirements.txt
- (Imagem) instala todas as dependências para rodar o container 

**Construir a imagem do Python:**

docker build -t imagem_conexao_mysql_aula_05 . (__criar container__)

**Rodar o container Python:**

docker run -d `
--name container_conexao_mysql_aula_05 `
--network rede_banco_mysql_aula_05 `
imagem_conexao_mysql_aula_05

Definições:
docker run → cria e executa um novo container.
-d → o container não executa de imediato.
--name container_conexao_mysql_aula_05 → dá um nome específico ao container. Sem isso, o Docker gera um nome aleatório.
--network rede_banco_mysql_aula_05 → conecta o container a uma rede Docker específica.
imagem_conexao_mysql_aula_05 → indica a imagem que será usada para criar o container.

__LISTAR CONTAINER__

docker ps -a

__RODAR CONTAINER__

docker start -ia container_conexao_mysql_aula_05
