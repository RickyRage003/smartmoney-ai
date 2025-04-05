import pandas as pd
from model.train_model import train_model

# Обучаем модель
model = train_model()

# Загружаем данные
df = pd.read_csv("data/sample_strategy.csv")

# Колонки, которые не используются как признаки
exclude = ["timestamp", "symbol", "entry_price", "exit_price", "result"]
feature_columns = [col for col in df.columns if col not in exclude]

# Извлекаем признаки
X = df[feature_columns]

# Предсказания
df["prediction"] = model.predict(X)
filtered = df[df["prediction"] == 1]

# Вывод результатов
print("✅ Оставлены сигналы:")
print(filtered[["timestamp", "symbol", "entry_price", "exit_price", "result"]])

# Сохраняем
filtered.to_csv("data/filtered_signals.csv", index=False)
