import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
import json

def train_model():
    df = pd.read_csv("data/sample_strategy.csv")
    
    # Целевая переменная
    y = df["result"]

    # Признаки (только числовые, исключаем result)
    X = df.drop(columns=["result"])
    X = X.select_dtypes(include=["number"])
    feature_columns = X.columns.tolist()

    # Обучение
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    accuracy = accuracy_score(y_test, model.predict(X_test))
    print(f"Accuracy: {accuracy:.4f}")

    # Сохраняем модель и признаки
    joblib.dump(model, "model/trade_filter.pkl")
    with open("model/feature_columns.json", "w") as f:
        json.dump(feature_columns, f)

    return model
