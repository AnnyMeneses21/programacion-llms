import pandas as pd
import numpy as np
import random
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

def generar_caso_de_uso_entrenar_clasificador_libros():

    n_samples = random.randint(20,50)
    n_features = random.randint(3,6)

    X = np.random.randn(n_samples,n_features)
    y = np.random.randint(0,2,size=n_samples)

    cols = [f"feature_{i}" for i in range(n_features)]

    df = pd.DataFrame(X,columns=cols)
    df["popularity_label"] = y

    target_col = "popularity_label"

    input_data = {
        "df": df.copy(),
        "target_col": target_col
    }

    X_data = df.drop(columns=[target_col])
    y_data = df[target_col]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X_data)

    model = DecisionTreeClassifier()
    model.fit(X_scaled,y_data)

    preds = model.predict(X_scaled)
    acc = accuracy_score(y_data,preds)

    output_data = (acc,preds)

    return input_data, output_data
