FROM python:3.11.9-alpine

ENV PYTHONUNBUFFERED 1
ENV PYTHONFAULTHANDLER 1

RUN mkdir /app
WORKDIR /app

RUN apk add \
    --no-cache \
    musl-dev linux-headers gcc g++ git gettext postgresql-dev jpeg-dev zlib-dev libffi-dev libxslt-dev gdal-dev geos-dev proj-dev nodejs yarn openssh

COPY requirements/dev.txt /app/
RUN python3 -m pip install --upgrade pip
RUN pip install --no-cache-dir -r dev.txt

ADD src /app/
# COPY src/ucsm_project /app/ucsm_project
# COPY src/ucsm_api /app/ucsm_api

# # Copiar manage.py a /app/ en la imagen
# COPY src/manage.py /app/
# COPY plataforma/src /app/src/
# COPY plataforma/statics /app/statics/

ARG VERSION
ENV VERSION $VERSION

RUN ls -la /app