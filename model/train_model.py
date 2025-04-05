import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

def train_model():
    df = pd.read_csv('data/sample_strategy.csv')

    # Отбрасываем ненужные колонки
    exclude_cols = ['timestamp', 'symbol', 'entry_price', 'exit_price', 'result']
    feature_cols = [col for col in df.columns if col not in exclude_cols]

    X = df[feature_cols]
    y = df['result']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    accuracy = model.score(X_test, y_test)
    return model, accuracy
