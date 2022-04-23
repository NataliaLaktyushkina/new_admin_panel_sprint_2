FROM python:3.10-alpine
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN set -ex \
  && apk --no-cache add postgresql-dev

WORKDIR /app

# для postgres
RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers

COPY /app/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app /app
RUN mkdir -p /static

COPY ./entrypoint.sh /
ENTRYPOINT ["sh","/entrypoint.sh"]

