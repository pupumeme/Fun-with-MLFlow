git clone https://github.com/pupumeme/Fun-with-MLFlow.git
cd Fun-with-MLFlow/
sudo docker build -t mlflow-docker . --no-cache
sudo docker run -p 5050:8888 mlflow-docker
