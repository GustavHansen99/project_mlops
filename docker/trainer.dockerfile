FROM nvcr.io/nvidia/pytorch:22.07-py3

RUN apt update

WORKDIR /
COPY requirements.txt requirements.txt
COPY src/ src/
COPY setup.py setup.py


RUN pip install --upgrade pip && \
    pip install wheel setuptools h5py typing && \
    pip install -r requirements.txt --no-cache-dir
