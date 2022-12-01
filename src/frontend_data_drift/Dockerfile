FROM python:3.10

EXPOSE 8502

COPY requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /app

COPY ./src .
COPY ./images .
