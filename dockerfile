FROM python:3.9

WORKDIR /code
COPY . /code

RUN apt-get update -qq
RUN apt-get install -y cmake
RUN apt-get install -y logrotate
RUN apt-get install -y gnupg
RUN rm -rf /var/lib/apt/lists/*

RUN pip3 install --no-cache-dir -r /code/requirements.txt

EXPOSE 4200
