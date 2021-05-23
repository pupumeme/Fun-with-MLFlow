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
```
chmod 777 run.sh
./run.sh
```

3. 開啟mlflow伺服器
```
mlflow server --backend-store-uri sqlite:///mlflow.db --default-artifact-root ./artifacts --host 0.0.0.0
```
(好像不能放進Dockerfile的樣子)


4. 記得把mlflow的檔案權限都設成可寫入
```
chmod 777 *
```


使用aws真的是當到不行，docker裝完竟然就要4GB，有夠肥  
我大概重架了快十個伺服器(ಥ_ಥ)  
後來才發現可以調storage的大小  
我哭了  

後來storage也無法解決  
最後把swap加大就行了  
https://askubuntu.com/questions/1264568/increase-swap-in-20-04  
搞了一整天，重架了十幾次(ಥ_ಥ)  
唯一的好處應該是讓我  
架docker和架mlflow變得很熟練...  
