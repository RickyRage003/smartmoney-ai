import pandas as pd
import joblib
import json
from model.train_model import train_model

model = train_model()

df = pd.read_csv("data/sample_strategy.csv")

# Загружаем признаки, на которых обучалась модель
with open("model/feature_columns.json", "r") as f:
    feature_columns = json.load(f)

features = df[feature_columns]
predictions = model.predict(features)

df["filtered"] = predictions
filtered = df[df["filtered"] == 1]

print("✅ Фильтрованные сигналы:")
print(filtered[["timestamp", "symbol", "entry_price", "exit_price", "result"]])

filtered.to_csv("data/filtered_signals.csv", index=False)
