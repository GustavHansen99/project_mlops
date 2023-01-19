FROM python:3.8-slim

WORKDIR /
COPY ./requirements_fastapi.txt /requirements_fastapi.txt
COPY ./app /app
COPY ./src /src
COPY ./config/infer.yaml /config/infer.yaml
COPY ./setup.py /setup.py

RUN pip install --upgrade pip
RUN pip install -r requirements_fastapi.txt --no-cache-dir

CMD ["python3", "./app/main.py"]
