FROM python:3.8-alpine
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN set -ex \
  && apk --no-cache add postgresql-dev

RUN mkdir -p /app
COPY ./app /app
WORKDIR /app

# для postgres
RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers

RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir -p /static

COPY ./entrypoint.sh /
ENTRYPOINT ["sh","/entrypoint.sh"]

