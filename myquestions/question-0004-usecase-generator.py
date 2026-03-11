import numpy as np
import random
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def generar_caso_de_uso_predecir_prestamos_libros():

    n_samples = random.randint(30,60)
    n_features = random.randint(2,5)

    X = np.random.rand(n_samples,n_features)
    y = np.random.rand(n_samples) * 10000

    input_data = {
        "X": X.copy(),
        "y": y.copy()
    }

    X_train,X_test,y_train,y_test = train_test_split(
        X,y,test_size=0.2,random_state=42
    )

    model = LinearRegression()
    model.fit(X_train,y_train)

    preds = model.predict(X_test)
    mse = mean_squared_error(y_test,preds)

    output_data = (mse,preds)

    return input_data, output_data
