git clone https://github.com/pupumeme/Fun-with-MLFlow.git
cd Fun-with-MLFlow/
sudo apt-get update -y 
sudo apt-get install docker.io -y 
sudo docker build -t mlflow-docker . --no-cache
sudo docker run -p 5050:8888 -p 5000:5000 -d mlflow-docker
