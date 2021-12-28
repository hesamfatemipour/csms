FROM ubuntu:20.04

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/Berlin
RUN apt update -y && apt install build-essential python-dev python3-pip uwsgi tzdata -y

COPY ./requirements.txt ./requirements.txt

ADD . /csms
WORKDIR /csms

RUN pip3 install -r requirements.txt

copy . /csms

RUN chmod +x ./entrypoint.sh

ENTRYPOINT ["./entrypoint.sh", "uwsgi"]