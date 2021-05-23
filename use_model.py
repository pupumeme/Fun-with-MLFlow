import mlflow
import mlflow.pyfunc
from sklearn.model_selection import train_test_split
from sklearn import datasets

mlflow.set_tracking_uri("http://127.0.0.1:5000")

# dataset
iris = datasets.load_iris()
x = iris.data[:, 2:]
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=7)

# load model
model_name = "my_iris_model"
model_version = 2

model = mlflow.pyfunc.load_model(
    model_uri=f"models:/{model_name}/{model_version}"
)

predictions = model.predict(X_test)

print(predictions)