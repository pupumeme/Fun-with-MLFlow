# Fun-with-MLFlow

image: https://hub.docker.com/r/jupyter/datascience-notebook/  
安裝docker: https://blog.gtwang.org/virtualization/ubuntu-linux-install-docker-tutorial/   
撰寫Dockerfile: https://ithelp.ithome.com.tw/articles/10191016   
mlflow教學:https://medium.com/@jain.roh/ml-flow-basic-approach-part-1-logging-e528a92922f5  
jupyter notebook之位址: http://3.36.66.201:5050/?token=ab1d1c8e8ef8216149adf6397e942d1f351c41e54e3fa8b4   
移除docker指令:https://blog.clarence.tw/2019/09/10/docker-removing-containers-images-volumes-and-networks/  

### MLflow伺服器之位址: http://3.36.66.201:5000
### 安裝docker
```
sudo apt-get install docker.io
```

### 執行Dockerfile
```
sudo docker build -t mlflow-docker . --no-cache  
sudo docker run -p 5050:8888 -p 5000:5000 -d mlflow-docker
```

###進入docker
```
sudo docker ps
sudo docker exec -it <container_id> bash
```
