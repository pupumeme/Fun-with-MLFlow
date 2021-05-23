git clone https://github.com/pupumeme/Fun-with-MLFlow.git
cd Fun-with-MLFlow/
sudo apt-get update -y 
sudo apt-get install docker.io -y 
sudo docker build -t mlflow-docker . --no-cache
