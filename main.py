import pandas as pd
from model.train_model import train_model
import joblib

# 1. Обучение модели (если не обучена)
model = train_model()

# 2. Загрузка сигналов
df = pd.read_csv("data/sample_strategy.csv")

# 3. Подготовка признаков
features = df[['feature1', 'feature2', 'feature3']]  # замените на актуальные названия

# 4. Фильтрация
predictions = model.predict(features)

# 5. Добавим колонку с результатом
df['filtered'] = predictions

# 6. Оставим только полезные сигналы
filtered_signals = df[df['filtered'] == 1]

# 7. Вывод результата
print("✅ Отфильтрованные сигналы:")
print(filtered_signals)

# 8. (опционально) Сохраняем
filtered_signals.to_csv("data/filtered_signals.csv", index=False)
