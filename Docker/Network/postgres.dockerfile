FROM postgres:13-alpine
LABEL maintainer "Kaique Gomes"
# Postgres environment variables 
ENV POSTGRES_HOST = fusion_db
ENV POSTGRES_USER = fusion_user
ENV POSTGRES_PASSWORD = fusion_pass
ENV POSTGRES_DB = fusion_app
EXPOSE 5432