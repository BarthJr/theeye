FROM python:3.9

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

RUN mkdir /theeye
WORKDIR /theeye
COPY ./theeye /theeye

RUN adduser user
USER user