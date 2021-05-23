# Fun-with-MLFlow

1. 把run.sh下載到伺服器
```
git clone https://github.com/pupumeme/Fun-with-MLFlow.git
cd Fun-with-MLFlow/
sudo apt-get update -y 
sudo apt-get install docker.io -y 
sudo docker build -t mlflow-docker . --no-cache
sudo docker run -p 5050:8888 -p 5000:5000 -d mlflow-docker
```

2. 執行run.sh

使用aws真的是當到不行，docker裝完竟然就要4GB，有夠肥  
我大概重架了快十個伺服器(ಥ_ಥ)  
