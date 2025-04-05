import pandas as pd
from model.train_model import train_model

# Загрузка данных
df = pd.read_csv('data/sample_strategy.csv')

# Обучаем модель
model, accuracy = train_model()

# Определяем признаки (автоматически, кроме excluded)
exclude_cols = ['timestamp', 'symbol', 'entry_price', 'exit_price', 'result']
feature_cols = [col for col in df.columns if col not in exclude_cols]

# Предсказываем
filtered = df.copy()
filtered['prediction'] = model.predict(df[feature_cols])
filtered = filtered[filtered['prediction'] == 1]

print("✅ Фильтрованные сигналы:")
print(filtered[['timestamp', 'symbol', 'entry_price', 'exit_price', 'result']])
print("🎯 Accuracy:", round(accuracy, 4))
