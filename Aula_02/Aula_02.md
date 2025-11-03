### Aula_02

### Teste CMD e ENTRYPOINT

**Com o Docker Desktop aberto**

---
- Dockerfile_cmd:

    __Criar Imagem:__
    ````
    docker build -t imagem_teste_cmd_aula_02 -f Dockerfile_cmd .    → Criar imagem
    ````
    __Saída: Sobrescrevi o CMD__
    ````
    docker run --name container__teste_cmd_aula_02 imagem_teste_cmd_aula_02    → Criar container
    docker container prune -f   →  Excluir container e para imagem
    ````
    __Saída: docker: Error...__
    ````
    docker run --name container__teste_cmd_aula_02 imagem_teste_cmd_aula_02 "Sobrescrevi o CMD"     → Criar container
    docker container prune -f   →  Excluir container e para imagem
    ````
    __Saída: Sobrescrevi o CMD__
    ````
    docker run --name container__teste_cmd_aula_02 imagem_teste_cmd_aula_02 echo "Sobrescrevi o CMD"    → Criar container
    docker container prune -f   →  Excluir container e para imagem
    ````
    <br>

    - Definição de parâmetro:
        - -f  → Força a execução do comando sem pedir confirmação.
---
<br>

- Dockerfile_entrypoint

    __Criar Imagem:__
    ````
    docker build -t imagem_teste_entrypoint_aula_02 -f Dockerfile_entrypoint .      →  Criar imagem
    ````
    - __Saída: Olá, eu sou o ENTRYPOINT__
    ````
    docker run --name container_teste_entrypoint_aula_02 imagem_teste_entrypoint_aula_02    →  Criar container
    docker container prune -f    →  Excluir container e para imagem
    ````
    - __Saída: Olá, eu sou o ENTRYPOINT echo TESTE__
    ````
    docker run --name container_teste_entrypoint_aula_02 imagem_teste_entrypoint_aula_02 echo "TESTE"   →  Criar container
    docker container prune -f    →  Excluir container e para imagem
    ````
    - __Saída: Olá, eu sou o ENTRYPOINT TESTE__
    ````
    docker run --name container_teste_entrypoint_aula_02 imagem_teste_entrypoint_aula_02 "TESTE"    →  Criar container
    docker container prune -f    →  Excluir container e para imagem
    ````
---
<br>

- Dockerfile_entrypoint_cmd

    __Criar Imagem:__
    ````
    docker build -t imagem_teste_entrypoint_cmd_aula_02 -f Dockerfile_entrypoint_cmd .      →  Criar imagem
    ````
    - __Saída: Olá, eu sou o CMD (argumento do ENTRYPOINT)__
    ````
    docker run --name container_teste_entrypoint_cmd_aula_02 imagem_teste_entrypoint_cmd_aula_02   →  Criar container
    docker container prune -f    →  Excluir container e para imagem
    ````
     
    - __Saída: echo Sobrescrevendo CMD__
    ````
    docker run imagem_teste_entrypoint_cmd_aula_02 echo "Sobrescrevendo CMD"    →  Criar container
    docker container prune -f    →  Excluir container e para imagem
    ````
    - __Saída: Sobrescrevendo CMD__
    ````
    docker run imagem_teste_entrypoint_cmd_aula_02 "Sobrescrevendo CMD"     →  Criar container
    docker container prune -f    →  Excluir container e para imagem
    ````
-----------------------------------------------------------------------------------------------------------------------------------

Resumo:
- Só CMD → Default flexível, fácil de trocar.
- Só ENTRYPOINT → Fixa o comando, só muda com --entrypoint.
- ENTRYPOINT + CMD → O mais poderoso: define um executável fixo e argumentos padrão que podem ser sobrescritos

````
docker build -t teste-cmd -f Dockerfile_cmd .
````
- Definições:
    - __docker build__ → Comando usado para construir uma imagem a partir de um Dockerfile.
    - __-t teste-entry__ → Define a tag da imagem (nome + versão).
        - Se você não colocar versão (:algo), o Docker assume :latest.
        - Aqui a imagem se chama teste-entry:latest.
    - __-f Dockerfile_entrypoint__ → Diz explicitamente qual arquivo Dockerfile usar.
        - Se você não usar -f, o Docker procura automaticamente um arquivo chamado Dockerfile no diretório.
    - __.__ → Define o build context: a pasta cujo conteúdo será enviado para o Docker Engine.
        - Esse contexto inclui o Dockerfile (se não foi passado via -f) e todos os arquivos que podem ser copiados com COPY ou ADD.