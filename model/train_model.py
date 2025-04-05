from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def train_model(X, y, base_df):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    accuracy = accuracy_score(y_test, model.predict(X_test))

    # Предсказания и фильтрация
    y_pred = model.predict(X)
    base_df["prediction"] = y_pred
    filtered = base_df[base_df["prediction"] == 1]

    return model, filtered, accuracy
