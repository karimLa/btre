FROM python:3.7-alpine

LABEL maintainer="Soramon0" version="1.0"

ENV PYTHONUNBUFFERED 1

COPY ./requirement.txt ./requirement.txt
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps \
  gcc libc-dev linux-headers postgresql-dev
RUN pip install --no-cache-dir -r /requirement.txt
RUN apk del .tmp-build-deps

WORKDIR /app
COPY ./app /app

RUN adduser -D user
USER user