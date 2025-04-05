import pandas as pd
from model.train_model import train_model
import matplotlib.pyplot as plt

# 1. Обучение
model = train_model()
df = pd.read_csv("data/sample_strategy.csv")

# 2. Признаки
exclude = ["timestamp", "symbol", "entry_price", "exit_price", "result"]
feature_columns = [col for col in df.columns if col not in exclude]
X = df[feature_columns]

# 3. Предсказания
df["prediction"] = model.predict(X)
filtered = df[df["prediction"] == 1]

# 4. Сохраняем
filtered.to_csv("data/filtered_signals.csv", index=False)

# 5. Визуализация
before = len(df)
after = len(filtered)
removed = before - after

plt.figure(figsize=(6, 4))
plt.bar(["До фильтрации", "После"], [before, after], color=["gray", "green"])
plt.title("Фильтрация сигналов")
plt.ylabel("Количество сделок")
plt.text(0, before + 1, f"{before}", ha='center')
plt.text(1, after + 1, f"{after}", ha='center')

plt.tight_layout()
plt.savefig("data/filter_chart.png")
print("📊 График сохранён как data/filter_chart.png")
