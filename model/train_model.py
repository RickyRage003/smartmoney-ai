import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

def train_model():
    df = pd.read_csv("data/sample_strategy.csv")

    # Целевая переменная
    y = df["result"]

    # Исключаем нефичевые столбцы
    exclude = ["timestamp", "symbol", "entry_price", "exit_price", "result"]
    feature_columns = [col for col in df.columns if col not in exclude]

    # Признаки
    X = df[feature_columns]

    # Обучение модели
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    accuracy = model.score(X_test, y_test)
    print(f"Accuracy: {accuracy:.4f}")

    return model
