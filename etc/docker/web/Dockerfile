# syntax=docker/dockerfile:1
FROM python:3.9-slim-bullseye

ENV PYTHONUNBUFFERED=1

RUN set -ex \
    && apt-get update \
    && apt-get install curl default-libmysqlclient-dev gcc -y \
    && rm -rf /var/lib/apt/lists/*

RUN useradd --create-home --shell /bin/bash --home /home/web web
USER web
WORKDIR /home/web

COPY etc/requirements.txt ./etc/requirements.txt

RUN set -ex \
    && python -m venv /home/web/venv \
    && ./venv/bin/pip install --upgrade pip \
    && ./venv/bin/pip install --no-cache-dir -r ./etc/requirements.txt

COPY etc/env ./etc/env

ENV VIRTUAL_ENV /home/web/venv
ENV PATH /home/web/venv/bin:$PATH
WORKDIR /home/web/server
