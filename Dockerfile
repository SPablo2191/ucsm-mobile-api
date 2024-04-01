FROM python:3


ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN mkdir /code
WORKDIR /code
COPY requirements/dev.txt /code/requirements/
RUN pip install -r requirements/dev.txt
ADD . /code/
EXPOSE 8000