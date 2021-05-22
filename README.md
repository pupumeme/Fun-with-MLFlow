# Fun-with-MLFlow

image: https://hub.docker.com/r/jupyter/datascience-notebook/  
安裝docker: https://blog.gtwang.org/virtualization/ubuntu-linux-install-docker-tutorial/   
撰寫Dockerfile: https://ithelp.ithome.com.tw/articles/10191016   
網址: http://18.234.225.184:5050/?token=dc4ac539e8a717fb425e4a23777c4ab4630e24477e2fe9f4  

### 安裝docker
```
sudo apt-get install docker.io
```

### Dockerfile  
```
FROM jupyter/datascience-notebook
USER root
RUN apt-get install python3-pip -y \
&&  pip3 install mlflow
```


### 執行Dockerfile
```
sudo docker build -t mlflow-docker . --no-cache  
sudo docker run -p 5050:8888 mlflow-docker
```

### run.sh
```
git clone https://github.com/pupumeme/Fun-with-MLFlow.git
cd Fun-with-MLFlow/
sudo apt-get update -y 
sudo apt-get install docker.io -y 
sudo docker build -t mlflow-docker . --no-cache
sudo docker run -p 5050:8888 mlflow-docker
```
