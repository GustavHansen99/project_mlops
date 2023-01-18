FROM nvidia/cuda:11.6.2-base-ubuntu20.04

USER root

# Install necessary packages for python.
# TODO: some/all of these could be avoided
RUN apt update && \
    apt upgrade -y && \
    apt install curl -y && \
    apt-cache search libcurl | grep

# install python 3.8 ans set it as default
RUN apt update && \
    apt install software-properties-common -y && \
    add-apt-repository ppa:deadsnakes/ppa -y && \
    apt install python3.8 && \
    alias python=python3


RUN apt install python-is-python3 -y
#&& \
#alias python=python3.8


#WORKDIR /
#COPY requirements.txt requirements.txt
#COPY src/ src/
#COPY setup.py setup.py


#RUN pip install -r requirements.txt --no-cache-dir
