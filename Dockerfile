FROM jupyter/pyspark-notebook:notebook-7.0.2
#FROM jupyter/pyspark-notebook:python-3.11
USER root

RUN apt-get update && \
    apt-get install -y curl vim wget git netcat graphviz && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir --upgrade pip setuptools

RUN pip install --no-cache-dir tensorflow && \
    pip install --no-cache-dir pydot && \
    pip install --no-cache-dir flask && \
    pip install --no-cache-dir numpy && \
    pip install --no-cache-dir pandas && \
    pip install --no-cache-dir matplotlib && \
    pip install --no-cache-dir kafka-python && \
    pip install --no-cache-dir confluent_kafka && \
    fix-permissions "/home/${NB_USER}" 

USER ${NB_USER}

WORKDIR /home/jovyan/notebooks
