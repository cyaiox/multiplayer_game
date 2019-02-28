FROM python:3.7.2-alpine
ENV PYTHONUNBUFFERED 1

WORKDIR /code

ADD requirements.txt .

RUN pip install -r requirements.txt

ADD ./src/ .

ENTRYPOINT python app.py
