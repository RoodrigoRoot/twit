FROM python:3.8-alpine AS Base

RUN mkdir app
WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update && apk add wget

COPY requirements.txt /app/
COPY . /app/

RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps \
      gcc libc-dev python3-dev linux-headers musl-dev postgresql-dev
RUN pip install -r requirements.txt
RUN apk del .tmp-build-deps



RUN adduser -D user
RUN mkdir -p /var/log/tweet
RUN chown -R user:user /var/log
RUN chown -R user:user /app
RUN chmod -R 755 /var/log/tweet

USER user
