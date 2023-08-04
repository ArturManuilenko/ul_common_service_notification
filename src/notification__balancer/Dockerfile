FROM library/nginx:1.19-alpine

COPY ./src/notification__balancer/remote /etc/nginx

WORKDIR /docker_app

COPY ./src/notification__web/static /docker_app/notification__web/static
