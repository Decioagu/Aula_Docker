Para ver seu IP:
````
ipconfig
````

Para ver sua rede Docker:
````
docker network ls 
````

Criar o arquivo HTML

Criar o Dockerfile

Executar o container novo container a partir do Dockerfile:
````
docker run -d -p 8080:80 --name webserver01 nginx:latest
````

Definições:
docker run → Cria e executa o container
-d → Roda em background
-p 8080:80 → Mapea host
--name webserver01 → Define nome do container
nginx:latest → Nome da imagem

Caso a porta este já ocupada, use porta 8081:80