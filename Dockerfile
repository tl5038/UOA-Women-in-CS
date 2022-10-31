FROM python:3.10-alpine

ENV PYTHONUNBUFFERED=1


ENV PATH="/docker:${PATH}"
ENV DJANGO_STATIC_ROOT="/data/www/static"
ENV DJANGO_MEDIA_ROOT="/data/www/media"

COPY requirements.txt ./
RUN apk add --update --no-cache --virtual .tmp  \
        gcc  \
        libc-dev  \
        linux-headers  \
        build-base  \
        musl-dev  \
        postgresql-dev && \
    pip install -r requirements.txt && \
    apk del .tmp && \
    apk add --no-cache postgresql-client && \
    mkdir /app

COPY ./src /app
WORKDIR /app
COPY ./docker /docker
RUN chmod +x /docker/* && \
    mkdir -p /data/www/media /data/www/static  && \
    adduser -D --no-create-home django && \
    chown -R django:django /data && \
    chmod -R 755 /data

USER django

EXPOSE 8000

CMD ["entrypoint.sh"]