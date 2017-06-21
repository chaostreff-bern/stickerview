FROM python:3.6.1-alpine

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
    && git clone https://github.com/chaostreff-bern/stickerview.git /app \
    && cd /app \
    && pip install /app \
    && pip install gunicorn \
    && apk del \
        git \
        gcc \
        musl-dev \
    && rm -rf /var/lib/apk/* /var/cache/apk/*

WORKDIR /app

EXPOSE 8080
VOLUME /app/data
CMD [ "gunicorn", "stickerview.wsgi", "-b", "0.0.0.0:8080" ]
