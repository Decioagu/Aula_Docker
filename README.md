# Aula_Docker

### Docker Container

**Docker é uma plataforma de virtualização leve usada principalmente no desenvolvimento de software para criar, executar e gerenciar aplicações em __containers__. Com o Docker, o ambiente é o mesmo em qualquer lugar: em sua máquina, no servidor ou na nuvem.**

Um __Container__ é como uma “caixinha” que empacota tudo o que a aplicação precisa para funcionar:
- O código-fonte
- Bibliotecas e dependências
- Configurações do sistema
- Ferramentas necessárias

**__Uma máquina virtual__ emula um sistema operacional inteiro, já o __Container compartilha o Kernel__ do Sistema Operacional, sendo muito mais leve e rápido.**
**Kernel (ou núcleo) é a parte central de um Sistema Operacional (Linux, Windows, etc.), que faz a ponte entre o hardware (processador, memória, dispositivos) e o software (aplicativos).**

Em Docker existe 4 conceitos básicos __Imagem__, __Container__, __Volume__ e __Rede__ onde:

__Imagem__ é um pacote imutável que contém tudo o que um container precisa para ser executado. Ela é construída a partir de instruções descritas em um arquivo Dockerfile. O Dockerfile não perde a utilidade após gerar a imagem, pois pode ser reutilizado para reconstruir ou atualizar a imagem sempre que necessário. Os containers são instâncias em execução criadas a partir dessa imagem.

__Container__ é a instância em execução de uma imagem. Ele representa um ambiente isolado que executa uma aplicação ou serviço, criado a partir de uma imagem Docker.

__Volume__ é a forma de armazenamento persistente no Docker. Ele mantém os dados mesmo que o container seja excluído e pode ser acessado por diferentes containers ao mesmo tempo, já que é gerenciado de forma independente do ciclo de vida do container. 

__Rede__ é um recurso de conectividade, que define como containers se comunicam entre si (bridge, host, overlay, etc.).

---
---

### Instalar no Windows

### Passo 1 - (PowerShell Admin):
- Pagina: https://learn.microsoft.com/pt-br/windows/wsl/setup/environment#set-up-your-linux-user-info- 
- wsl --install
--- 

### Passo 2 - REINICIE O COMPUTADOR e em WSL

-------------------------------------------------- WSL --------------------------------------------------

- Ubuntu já está instalado.
- Iniciando Ubuntu...
- Installing, this may take a few minutes...
- Please create a default UNIX user account. The username does not need to match your Windows username.
- For more information visit: https://aka.ms/wslusers
- Enter new UNIX username: deciosan <--------------------
- New password: decioagu <--------------------------------
- Retype new password:
- passwd: password updated successfully
- Installation successful!
- To run a command as administrator (user "root"), use "sudo <command>".
- See "man sudo_root" for details.
----------------------------------------------------------------------------------------------------------

### Passo 3 - (Instalar Docker Desktop):
- Tutorial: https://docs.docker.com/docker-for-windows/install/
- Instale o capote para windows
---

### Passo 4 - Testar se está funcionando
- docker --version
- docker run hello-world (__Criar container a partir da imagem padão já existente no Docker__)

---
---
---

### Aula_01
### 1º - Crie seu programa PYTHON
Exemplo: 
- Pasta: Aula_01
- Arquivo: calculo_imc.py
---

### 2º - Criar o Dockerfile
No seu projeto, crie um arquivo chamado Dockerfile (sem extensão). Exemplo simples com Python:

- Definições:
    - FROM → define a imagem base (ex: um Linux com Python, Node, etc.).
    - LABEL → serve para adicionar metadados à imagem Docker, informações extras na imagem.
    - WORKDIR → cria e define o diretório de trabalho dentro do container para execução do programa.
    - COPY / ADD → copia arquivos do seu PC para dentro da imagem.
    - RUN → executa comandos na construção da imagem (instalação de pacotes).
    - EXPOSE → serve para documentar quais portas a aplicação dentro do container vai escutar.
    - ENV → serve para definir variáveis de ambiente dentro da imagem/container.
    - EXPOSE → documenta a porta que o container vai expor.
    - CMD → define o comando padrão que o container vai rodar.
    - ENTRYPOINT → define o programa principal que será executado sempre que o container iniciar.

Exemplo Dockerfile:
FROM python:3.12-slim
LABEL maintainer="Decio <decio@email.com>"
LABEL version="1.0"
LABEL description="Imagem para calcular IMC com Python"
WORKDIR /app/
COPY calculo_imc.py /app
CMD ["python", "calculo_imc.py"] 

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
- Com o Docker Desktop aberto
- cd C:\caminho\do\projeto
- docker build -t __NOME DA IMAGEM__ -f __NOME DO ARQUIVO DOCKERFILE PERSONALIZADO__.

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


Exemplo:
Com o Docker Desktop aberto
cd C:\REPOSITORIO\Aula_Docker\Aula_01
docker build -t imagem_calculo_imc_aula_01 .
---

### 4º - Ver imagem ou ler arquivo Dockerfile
Esteja no diretório atual e execute:
- Com o Docker Desktop aberto
- docker ps (__listar todas as imagens em Docker Desktop em execução__)
- docker ps -a (__listar todas as imagens existente em Docker Desktop__)
- docker ps -aq (__listar todas os ID das imagens existente em Docker Desktop__)
- docker images (__listar todas as imagens existente em Docker Desktop__)
- cat Dockerfile (__ler arquivo Dockerfile da pasta atual__)
---- 

### 5º - Cria e iniciar um container a partir de uma imagem
Esteja no diretório atual e execute:
- Com o Docker Desktop aberto
- docker run -it -- name __NOME DO CONTAINER__ __NOME DA IMAGEM__ 

- Definição de parâmetros:
    - --name → nomear container
    - -d → rodar em background
    - -p → mapear portas
    - -v → volumes/persistência
    - -e → variáveis de ambiente
    - -it → interativo/terminal
    - --rm → remove ao parar
    - --network → conecta a rede

Exemplo:
- Com o Docker Desktop aberto
- docker images (__lista de todas as imagens existente no Docker Desktop__)
- docker run -it --name container_calculo_imc_aula_01 imagem_calculo_imc_aula_01
---

### 6º - Executar container criado
- Com o Docker Desktop aberto
- docker start -ai container_calculo_imc_aula_01
- docker exec container_calculo_imc_aula_01 bash
    - Definições:
        - docker start → só inicia o container, sem comandos novos.
        - docker exec → só inicia o container, com outros comandos (ex: echo, bash, etc).

### 7º - Parar execução de imagem
Listar todos os containers (ativos e parados).
- Com o Docker Desktop aberto
- docker images (__lista de todas as imagens existente no Docker Desktop__)
- docker ps (__lista de imagem em execução__)
- docker ps -a (__lista de imagem já ativadas__)

Exemplo de lista: 
- CONTAINER ID   IMAGE                     COMMAND                  CREATED         
- 0746564a0197   imagem_calculo_imc_aula_01       "python calculo_imc.…"   8 minutes ago    

### 8º - Para execução de um container
- Com o Docker Desktop aberto
- docker stop __ID OU NOME DO CONTAINER__

- Definições:
    - docker container prune → exclui container não usadas.
    - docker image prune → parar imagens não usadas.
    - docker volume prune → parar volumes não utilizados.
    - docker network prune → parar redes não usadas.
    - docker system prune → limpa tudo de uma vez (containers parados, imagens órfãs, redes não usadas,volumes anônimos).
---

### 9º - Excluir imagem
Excluir imagem:
- Com o Docker Desktop aberto
- docker rmi __ID OU NOME DA IMAGEM__ (Excluir imagem - NÃO pode estrar em execução)
---

### 10º - Excluir container
Excluir container:
- Com o Docker Desktop aberto
- docker rm __ID OU NOME DO CONTAINER__ (Excluir container - NÃO pode estrar em execução)

### 11º - Informações detalhadas da imagem em formato JSON
Imagem em formato JSON:
- Com o Docker Desktop aberto
- docker inspect __ID__
- docker inspect __NOME DO ARQUIVO__

---
---
---

### Aula_02
### Teste CMD e ENTRYPOINT

Em arquivos Dockerfile: qual a diferença entre CMD e ENTRYPOINT ao criar uam imagem?

CMD:
Define o comando padrão que será executado quando um container da imagem for iniciado.
Pode ser sobrescrito facilmente quando você usa docker run <imagem> <comando>.

ENTRYPOINT:
Define o processo principal do container (o executável fixo).
Diferente do CMD, não é sobrescrito por argumentos no docker run.
Mas você pode passar parâmetros extras ao comando.

CMD + ENTRYPOINT: 
Você pode usar os dois.
ENTRYPOINT define o comando fixo.
CMD define parâmetros padrão que podem ser sobrescritos.

Dica prática:
Use CMD quando quiser flexibilidade (comando padrão, mas pode trocar).
Use ENTRYPOINT quando o container for sempre rodar um executável principal (ex.: nginx, python).
Use os dois juntos para dar parâmetros padrão mas ainda permitir sobrescrever.

Segue exemplo: [Aula_02](Aula_02/Aula_02.md)

---
---
---


### Aula_03
### Rodar imagem em tempo real

- Criar o programa Python (__olamundo.py__)
- Criar o Dockerfile
- docker build -t imagem_ola_mundo_aula_03 .   (__Criar imagem__)
- docker run -it --name container_ola_mundo_aula_03 imagem_ola_mundo_aula_03   (__Criar container e rodar em tempo real "it"__)
    - -i → mantém o terminal interativo (interactive).
    - -t → Cria terminal virtual (tty) para saída formatada.
- docker start -ai container_ola_mundo_aula_03 (__Rodar container em tempo real "-ai"__)
    - -a → conecta a saída do container ao seu terminal (attach).
    - -i → mantém o terminal interativo (interactive).
- docker container prune -f (__excluir container e para imagem__)

---
---
---


### Aula_04
### Volumes SQLite

- Um Volume é um espaço de armazenamento gerenciado pelo Docker, que fica fora do ciclo de vida do container. Mesmo que o container seja apagado, o volume continua existindo, ou seja, outro container pode usar o mesmo volume. É como um HD externo que você conecta e desconecta de containers.

**Criar um volume**
docker volume create volume_meus_dados

**Criar duas redes**
docker network create rede_a
docker network create rede_b

**Container 1 com volume e conectado à rede_a**
docker run -d --name c1 --network rede_a -v volume_meus_dados:/app/data busybox sleep 3600

**Container 2 com mesmo volume mas na rede_b**
docker run -d --name c2 --network rede_b -v volume_meus_dados:/app/data busybox sleep 3600

**Container 3 com mesmo volume mas sem rede nenhuma**
docker run -d --name c3 --network none -v volume_meus_dados:/app/data busybox sleep 3600

Criação de Volume com banco de dados SQLite.
Neste exemplo temos um container conectado a um volume sem intermediação de uma rede.

Segue exemplo: [Aula_04](Aula_04/Aula_04.md)

---
---
---


### Aula_05
### Volumes MySQL

Criação de Volume com banco de dados MySQL.
Neste exemplo temos um volume conectado a um container por meio de uma rede.

---
---
---

### Aula_06
### __Host → phpMyAdmin → MySQL__

Neste exemplo temos 3 container (MySQL, phpMyAdmin, wordpress) interligada por uma rede.

[Aula_06](Aula_06/Aula_06.md)

===================================================================================
