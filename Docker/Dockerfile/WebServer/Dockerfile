# Base image to create yout new custom image
FROM nginx:1.19.4-alpine

# How is mainteining this image
LABEL maintainer="Kaique Viana"

# Copy all itens from the base directory to the container dir
COPY . /usr/share/nginx/html

# Expose a port to my use 
EXPOSE 80
