# Fun-with-MLFlow

image: https://hub.docker.com/r/jupyter/datascience-notebook/  
安裝docker: https://blog.gtwang.org/virtualization/ubuntu-linux-install-docker-tutorial/   
撰寫Dockerfile: https://ithelp.ithome.com.tw/articles/10191016   
mlflow教學:https://medium.com/@jain.roh/ml-flow-basic-approach-part-1-logging-e528a92922f5  
網址: http://3.36.66.201:5050/?token=7614db766f3706db90db1f0859912dcb5fb708e053b76297  

### 安裝docker
```
sudo apt-get install docker.io
```

### Dockerfile  
```
FROM jupyter/datascience-notebook
USER root
RUN apt-get install python3-pip -y \
&&  pip3 install mlflow -y \
&& sudo docker run -p 5050:8888 -d mlflow-docker
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
```

###進入docker
```
docker ps
docker exec -it <container_id> bash
```
