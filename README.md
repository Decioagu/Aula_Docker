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
---

### Instalar no Windows

### Passo 1 - (PowerShell Admin):
- Pagina: https://learn.microsoft.com/pt-br/windows/wsl/setup/environment#set-up-your-linux-user-info- 
````
wsl --install
````
--- 

### Passo 2 - REINICIE O COMPUTADOR e em WSL

-------------------------------------------------- WSL --------------------------------------------------
````
Ubuntu já está instalado.
Iniciando Ubuntu...
Installing, this may take a few minutes...
Please create a default UNIX user account. The username does not need to match your Windows username.
For more information visit: https://aka.ms/wslusers
Enter new UNIX username: deciosan <--------------------
New password: decioagu <--------------------------------
Retype new password:
passwd: password updated successfully
Installation successful!
To run a command as administrator (user "root"), use "sudo <command>".
See "man sudo_root" for details.
````
----------------------------------------------------------------------------------------------------------

### Passo 3 - (Instalar Docker Desktop):
- Tutorial: https://docs.docker.com/docker-for-windows/install/
- Instale o capote para windows
---

### Passo 4 - Testar se está funcionando
````
docker --version
docker run hello-world (__Criar container a partir da imagem padão já existente no Docker__)
````
---
---
---

### Aula_01
- Criar o Dockerfile
- Criar a imagem
- Visualizar imagem
- Cria container
- Executar container
- Parar execução de imagem
- Para execução de um container
- Excluir imagem
- Excluir container
- Informações detalhadas da imagem em formato JSON

### Link: [Criação de container e imagens Aula_01](Aula_01/Aula_01.md)

---

### Aula_02
### Teste CMD e ENTRYPOINT

- Em arquivos Dockerfile: 
    - Qual a diferença entre CMD e ENTRYPOINT ao criar uam imagem?

- CMD:
    - Define o comando padrão que será executado quando um container da imagem for iniciado.
    - Pode ser sobrescrito facilmente quando você usa docker run <imagem> <comando>.

- ENTRYPOINT:
    - Define o processo principal do container (o executável fixo).
    - Diferente do CMD, não é sobrescrito por argumentos no docker run.
    - Mas você pode passar parâmetros extras ao comando.

- CMD + ENTRYPOINT: 
    - Você pode usar os dois.
    - ENTRYPOINT define o comando fixo.
    - CMD define parâmetros padrão que podem ser sobrescritos.

- Dica prática:
    - Use CMD quando quiser flexibilidade (comando padrão, mas pode trocar).
    - Use ENTRYPOINT quando o container for sempre rodar um executável principal (ex.: nginx, python).
    - Use os dois juntos para dar parâmetros padrão mas ainda permitir sobrescrever.

### Link: [Diferença entre CMD e ENTRYPOINT Aula_02](Aula_02/Aula_02.md)

---

### Aula_03
### Rodar imagem em tempo real

- Criar o programa Python →   (__olamundo.py__)
- Criar o Dockerfile
````
docker build -t imagem_ola_mundo_aula_03 .   →  Criar imagem
docker run -it --name container_ola_mundo_aula_03 imagem_ola_mundo_aula_03   → Criar container e rodar em tempo real "it"
````
- Definição de parâmetros:
    - -i → Mantém o terminal interativo (interactive).
    - -t → Cria terminal virtual (tty) para saída formatada.
````
docker start -ai container_ola_mundo_aula_03    →  Rodar container em tempo real "-ai"
````
- Definição de parâmetros:
    - -a → Conecta a saída do container ao seu terminal (attach).
    - -i → Mantém o terminal interativo (interactive).
````
docker container prune -f   →  Excluir container e para imagem
````
- Definição de parâmetro:
    - -f  → Força a execução do comando sem pedir confirmação.

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
