FROM nvcr.io/nvidia/pytorch:22.07-py3

RUN apt update

WORKDIR /Github
COPY requirements.txt requirements.txt

RUN pip install --upgrade pip && \
    pip install -r requirements.txt --no-cache-dir

COPY src/ src/
COPY setup.py setup.py
COPY .dvc/ .dvc/
COPY .git/ .git/
COPY data.dvc data.dvc
COPY config/ config/
COPY scripts/ scripts/

# local package
RUN pip install -e .

# Make train script executable
RUN chmod +x scripts/train.sh

ENTRYPOINT [ "scripts/train.sh" ]
