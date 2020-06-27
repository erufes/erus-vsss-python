FROM ubuntu:18.04

ARG DEBIAN_FRONTEND=noninteractive

RUN apt update

RUN apt install git python3-pip -y

COPY . /erus-vss-python

WORKDIR /erus-vss-python

RUN git clone https://github.com/erufes/VSS-CorePy.git

RUN chmod +x /erus-vss-python/VSS-CorePy/configure.sh

WORKDIR /erus-vss-python/VSS-CorePy

RUN /erus-vss-python/VSS-CorePy/configure.sh

WORKDIR /erus-vss-python

RUN pip3 install zmq protobuf

ENTRYPOINT "python3 /erus-vss-python/simulador.py"


