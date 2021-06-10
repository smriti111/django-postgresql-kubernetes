FROM python:3.9-alpine

ENV PYTHONBUFFERED 1

COPY requirements.txt .
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .temp-build-deps \
        && apk add gcc libc-dev linux-headers postgresql-dev \
        && pip install --upgrade pip \
        && pip install -r requirements.txt \
        && apk del .temp-build-deps


RUN mkdir app
WORKDIR /app
COPY . /app
EXPOSE 8010
CMD ["python","manage.py","runserver","0.0.0.0:8010"]
