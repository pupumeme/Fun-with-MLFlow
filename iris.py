import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn import datasets

# uncomment portion below if using a remote mlflow instance
# mlflow.set_tracking_uri("http://your-server:5000")
iris = datasets.load_iris()
x = iris.data[:, 2:]
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=7)

mlflow.set_tracking_uri("http://127.0.0.1:5000")
    
# add parameters for tuning
num_estimators = 3
mlflow.log_param("num_estimators",num_estimators)

# train the model
rf = RandomForestRegressor(n_estimators=num_estimators)
rf.fit(X_train, y_train)
predictions = rf.predict(X_test)

# Model Registry
mlflow.sklearn.log_model(
    sk_model=rf,
    artifact_path="sklearn-model",
    registered_model_name="my_iris_model"
)

# log model performance 
mse = mean_squared_error(y_test, predictions)
mlflow.log_metric("mse", mse)
print("  mse: %f" % mse)

mlflow.end_run()
print(mlflow.get_artifact_uri())