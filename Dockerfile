FROM python:3.7-alpine

LABEL maintainer="Soramon0" version="1.0"

ENV PYTHONUNBUFFERED 1

COPY ./requirement.txt ./requirement.txt
RUN pip install --no-cache-dir -r /requirement.txt

WORKDIR /app
COPY ./app /app

RUN adduser -D user
USER user