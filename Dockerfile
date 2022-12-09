FROM python:3.8-alpine3.17
WORKDIR /app

COPY requirements.txt requirements.txt

RUN apk update && apk add python3-dev \
                        gcc \
                        libc-dev

RUN apk add g++


RUN pip3 install --upgrade pip

RUN pip3 install mmh3
RUN pip3 install -r requirements.txt

COPY . .

RUN chmod -R 777 /app


CMD ["python3", "/app/main.py"]
