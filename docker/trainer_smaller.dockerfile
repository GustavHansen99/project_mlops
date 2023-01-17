FROM trainer_smaller:latest
#FROM nvidia/cuda:11.6.2-base-ubuntu20.04

USER root
#RUN sudo apt update && \
#    sudo apt install software-properties-common && \
RUN apt update && \
    apt upgrade -y && \
    apt install curl -y && \
    apt-cache search libcurl | grep python && \
    apt install python3-pycurl -y && \
    distribution=$(. /etc/os-release;echo $ID$VERSION_ID) \
    && curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg \
    && curl -s -L https://nvidia.github.io/libnvidia-container/$distribution/libnvidia-container.list | \
    sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
    tee /etc/apt/sources.list.d/nvidia-container-toolkit.list && \
    apt update && \
    apt install -y nvidia-docker2 -y

WORKDIR /
COPY requirements.txt requirements.txt
COPY src/ src/
COPY setup.py setup.py


#RUN pip install -r requirements.txt --no-cache-dir
