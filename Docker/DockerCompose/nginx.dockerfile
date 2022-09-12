FROM nginx:1.19.4-alpine
ENV PYTHONUBUFFERED 1
ENV LANG C.UTF-8
ENV DEBIAN_FRONTEND = noninteractive
COPY Fusion/config/nginx.conf /etc/nginx/nginx.conf
COPY Fusion/* /var/www
EXPOSE 80 443
ENTRYPOINT [ "nginx" ]
CMD [ "-g","deamon off;" ]