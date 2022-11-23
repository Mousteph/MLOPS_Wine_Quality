FROM python:3.10

EXPOSE 80

COPY requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /code
COPY ./src .
