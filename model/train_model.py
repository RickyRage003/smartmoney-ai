import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def train_model():
    df = pd.read_csv("data/sample_strategy.csv")

    # Отделим целевую переменную
    y = df["result"]

    # Удалим целевую и нечисловые признаки
    X = df.drop(columns=["result"])
    X = X.select_dtypes(include=["number"])  # оставим только числовые колонки

    # Сплитим данные
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    acc = accuracy_score(y_test, predictions)
    print(f"Accuracy: {acc:.4f}")

    return model
