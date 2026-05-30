FROM apache/airflow:2.9.1

USER root

RUN apt-get update && apt-get install -y docker.io
ARG DOCKER_GID=984 
# pass result to DOCKER_GID from getent group docker | cut -d: -f3

RUN groupadd -g $DOCKER_GID docker-host && \
    usermod -aG docker-host airflow

USER airflow

COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt