FROM python:3.8-alpine
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

USER root

RUN mkdir -p /app
COPY ./app /app
#RUN apk add postgresql-dev=9.6.10-r0 \
#    --repository=http://dl-cdn.alpinelinux.org/alpine/v3.5/main

RUN set -ex \
  && apk --no-cache add \
    postgresql-dev

RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers

WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt
RUN apk del .tmp

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static


