FROM jupyter/datascience-notebook
USER root
RUN sudo apt-get update \ 
&& sudo apt-get install python3-pip -y \
&& pip3 install mlflow \
&& sudo apt-get install docker.io -y \
&& sudo docker run -p 5050:8888 -p 5000:5000 -d mlflow-docker
