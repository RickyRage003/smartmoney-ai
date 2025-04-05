import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib
import os

def train_model():
    # Загрузка данных
    df = pd.read_csv("data/sample_strategy.csv")

    # Проверка структуры
    if df.shape[1] < 2:
        raise ValueError("CSV должен содержать как минимум одну фичу и один целевой столбец.")

    # Предположим, что последний столбец — target
    X = df.iloc[:, :-1].astype(float)
    y = df.iloc[:, -1].astype(int)

    # Разделение данных
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Обучение модели
    clf = RandomForestClassifier()
    clf.fit(X_train, y_train)

    # Оценка точности
    y_pred = clf.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Accuracy: {accuracy:.4f}")

    # Сохранение модели
    os.makedirs("model", exist_ok=True)
    joblib.dump(clf, "model/model.pkl")
