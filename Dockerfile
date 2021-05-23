FROM jupyter/datascience-notebook
USER root
RUN apt-get install python3-pip -y \
&&  pip3 install mlflow -y \
&& sudo docker run -p 5050:8888 -p 5000:5000 -d mlflow-docker
