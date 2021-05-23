FROM jupyter/datascience-notebook
USER root
RUN sudo apt-get update \ 
&& sudo apt-get install python3-pip -y \
&& pip3 install mlflow \
&& mlflow server --backend-store-uri sqlite:///mlflow.db --default-artifact-root ./artifacts --host 0.0.0.0 &
