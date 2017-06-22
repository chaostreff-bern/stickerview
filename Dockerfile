FROM python:3.6.1-alpine

COPY . /host/
RUN apk update \
    && apk upgrade \
    && apk add --no-cache \
        git \
        zlib-dev \
        jpeg-dev \
        gcc \
        musl-dev \
        postgresql-dev \
        mariadb-dev \
    && mkdir -p /app \
    && cd /app \
    && pip install --compile /host[mysql,pgsql] \
    && pip install gunicorn \
    && apk del \
        git \
        gcc \
        musl-dev \
    && rm -rf /host \
    && rm -rf /var/lib/apk/* /var/cache/apk/*

WORKDIR /app

EXPOSE 8080
VOLUME /app/data
CMD [ "gunicorn", "stickerview.wsgi", "-b", "0.0.0.0:8080" ]
