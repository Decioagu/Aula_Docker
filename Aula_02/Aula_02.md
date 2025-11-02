### Aula_02
### Teste CMD e ENTRYPOINT

**Dentro da pasta Aula_02**
- Com o Docker Desktop aberto

- Dockerfile_cmd:
    __Criar Imagem:__
    - docker build -t imagem_teste_cmd_aula_02 -f Dockerfile_cmd .   (__criar imagem__)

    - __Saída: Sobrescrevi o CMD__
    - docker run --name container__teste_cmd_aula_02 imagem_teste_cmd_aula_02   (__criar container__)
    - docker container prune -f (__excluir container e para imagem__)

    - __Saída: docker: Error...__
    - docker run --name container__teste_cmd_aula_02 imagem_teste_cmd_aula_02 "Sobrescrevi o CMD" (__criar container__)
    - docker container prune -f (__excluir container e para imagem__)

    - __Saída: Sobrescrevi o CMD__
    - docker run --name container__teste_cmd_aula_02 imagem_teste_cmd_aula_02 echo "Sobrescrevi o CMD" (__criar container__)
    - docker container prune -f (__excluir container e para imagem__)
    
OBS: Funcionou porque echo existe dentro do Ubuntu e sabe lidar com o argumento "============== Sobrescrevi o CMD ==============".

-----------------------------------------------------------------------------------------------------------------------------------

- Dockerfile_entrypoint

    __Criar Imagem:__
    - docker build -t imagem_teste_entrypoint_aula_02 -f Dockerfile_entrypoint .  (__criar imagem__)

    - __Saída: Olá, eu sou o ENTRYPOINT__
    - docker run --name container_teste_entrypoint_aula_02 imagem_teste_entrypoint_aula_02   (__criar container__)
    - docker container prune -f (__excluir container e para imagem__)

    - __Saída: Olá, eu sou o ENTRYPOINT echo TESTE__
    - docker run --name container_teste_entrypoint_aula_02 imagem_teste_entrypoint_aula_02 echo "TESTE" (__criar container__)
    - docker container prune -f (__excluir container e para imagem__)

    - __Saída: Olá, eu sou o ENTRYPOINT TESTE__
    - docker run --name container_teste_entrypoint_aula_02 imagem_teste_entrypoint_aula_02 "TESTE" (__criar container__)
    - docker container prune -f (__excluir container e para imagem__)

-----------------------------------------------------------------------------------------------------------------------------------

- Dockerfile_entrypoint_cmd

    __Criar Imagem:__
    - docker build -t imagem_teste_entrypoint_cmd_aula_02 -f Dockerfile_entrypoint_cmd .  (__criar imagem__)

    - __Saída: Olá, eu sou o CMD (argumento do ENTRYPOINT)__
    - docker run --name container_teste_entrypoint_cmd_aula_02 imagem_teste_entrypoint_cmd_aula_02   (__criar container__)
    - docker container prune -f (__excluir container e para imagem__)
     
    - __Saída: echo Sobrescrevendo CMD__
    - docker run imagem_teste_entrypoint_cmd_aula_02 echo "Sobrescrevendo CMD" (__criar container__)
    - docker container prune -f (__excluir container e para imagem__)

    - __Saída: Sobrescrevendo CMD__
    - docker run imagem_teste_entrypoint_cmd_aula_02 "Sobrescrevendo CMD" (__criar container__)
    - docker container prune -f (__excluir container e para imagem__)
    
-----------------------------------------------------------------------------------------------------------------------------------

Resumo:
- Só CMD → default flexível, fácil de trocar.
- Só ENTRYPOINT → fixa o comando, só muda com --entrypoint.
- ENTRYPOINT + CMD → o mais poderoso: define um executável fixo e argumentos padrão que podem ser sobrescritos


- docker build -t teste-cmd -f Dockerfile_cmd .
    - Definições:
        - __docker build__ → comando usado para construir uma imagem a partir de um Dockerfile. ✅
        - __-t teste-entry__ → define a tag da imagem (nome + versão).
            - Se você não colocar versão (:algo), o Docker assume :latest.
            - Aqui a imagem se chama teste-entry:latest. ✅
        - __-f Dockerfile_entrypoint__ → diz explicitamente qual arquivo Dockerfile usar.
            - Se você não usar -f, o Docker procura automaticamente um arquivo chamado Dockerfile no diretório. ✅
        - __.__ → define o build context: a pasta cujo conteúdo será enviado para o Docker Engine.
            - Esse contexto inclui o Dockerfile (se não foi passado via -f) e todos os arquivos que podem ser copiados com COPY ou ADD.