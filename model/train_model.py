import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib

def train_model(csv_path='data/sample_strategy.csv', model_path='model/model.pkl'):
    df = pd.read_csv(csv_path)
    if 'signal' not in df.columns:
        print("Missing 'signal' column in dataset.")
        return

    X = df.drop(columns=['signal'])
    y = df['signal']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    print(classification_report(y_test, preds))

    joblib.dump(model, model_path)
