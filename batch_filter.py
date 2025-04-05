import os
import pandas as pd
from model.train_model import train_model

# Исключаемые файлы
EXCLUDE = ['filtered_signals.csv', 'filter_chart.png']

# 1. Обучение на sample_strategy.csv
model = train_model()

# 2. Проходим по всем CSV в data/
for file in os.listdir("data"):
    if file.endswith(".csv") and not file.endswith("_filtered.csv") and file not in EXCLUDE:
        path = f"data/{file}"
        df = pd.read_csv(path)

        # Выбор признаков
        exclude = ["timestamp", "symbol", "entry_price", "exit_price", "result"]
        feature_columns = [col for col in df.columns if col not in exclude]

        if not all(col in df.columns for col in feature_columns):
            print(f"⚠️ Пропущено: {file} (нет нужных признаков)")
            continue

        try:
            filtered = df.copy()
            filtered["prediction"] = model.predict(df[feature_columns])
            filtered = filtered[filtered["prediction"] == 1]

            # Сохранение нового файла
            output_path = f"data/{file.replace('.csv', '_filtered.csv')}"
            filtered.to_csv(output_path, index=False)
            print(f"✅ Сохранён: {output_path}")
        except Exception as e:
            print(f"❌ Ошибка в {file}: {e}")
