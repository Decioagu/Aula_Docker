FROM nginx:latest

# Criar um usuário não-root
RUN addgroup --system --gid 1001 nginx_group && \
    adduser --system --uid 1001 --ingroup nginx_group --no-create-home nginx_user

# Criar diretórios necessários e ajustar permissões
RUN mkdir -p /var/cache/nginx && \
    mkdir -p /var/log/nginx && \
    mkdir -p /usr/share/nginx/html && \
    chown -R nginx_user:nginx_group /var/cache/nginx && \
    chown -R nginx_user:nginx_group /var/log/nginx && \
    chown -R nginx_user:nginx_group /usr/share/nginx/html

# Ajustar permissões do diretório de configuração
RUN touch /var/run/nginx.pid && \
    chown -R nginx_user:nginx_group /var/run/nginx.pid

# Copiar arquivos HTML
COPY --chown=nginx_user:nginx_group ./html /usr/share/nginx/html

# Permitir que o Nginx se vincule à porta 80
RUN setcap 'cap_net_bind_service=+ep' /usr/sbin/nginx

EXPOSE 80

# Configurar o Nginx para usar o usuário não-root
RUN sed -i 's/user\s*nginx;/user nginx_user;/g' /etc/nginx/nginx.conf

# Mudar para usuário não-root
USER nginx_user

CMD ["nginx", "-g", "daemon off;"]