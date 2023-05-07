FROM jupyter/pyspark-notebook

USER root

RUN apt-get update && \
    apt-get install -y curl vim wget git netcat && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

RUN conda install --no-cache tensorflow pymongo flask numpy pandas matplotlib --yes

USER ${NB_UID}

WORKDIR /home/jovyan/notebooks
