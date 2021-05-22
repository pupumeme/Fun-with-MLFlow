FROM jupyter/datascience-notebook
USER root
RUN apt-get update -y \
&&  apt-get install python3-pip -y \
&&  pip3 install mlflow
