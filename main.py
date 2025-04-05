import pandas as pd
import matplotlib.pyplot as plt
from model.train_model import train_model
from telegram_bot import send_telegram_report

# Загрузка данных
file_path = 'data/sample_strategy.csv'
df = pd.read_csv(file_path)

# Предобработка данных (удаляем нечисловые признаки)
X = df.select_dtypes(include=['number']).drop(columns=['result'])
y = df['result']

# Обучение и фильтрация модели
model, filtered, accuracy = train_model(X, y, df)
print(f"\n✅ Фильтрованные сигналы:")
print(filtered)
print(f"Accuracy: {accuracy:.4f}")

# Сохраняем отфильтрованные сигналы
filtered.to_csv('data/filtered_signals.csv', index=False)

# Строим график PnL
filtered['pnl'] = filtered['exit_price'] - filtered['entry_price']
filtered['cumulative_pnl'] = filtered['pnl'].cumsum()

plt.figure(figsize=(10, 5))
plt.plot(filtered['timestamp'], filtered['cumulative_pnl'], marker='o')
plt.title('Cumulative PnL')
plt.xlabel('Timestamp')
plt.ylabel('PnL')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('data/filter_chart.png')
plt.close()

# Отправляем Telegram-отчёт
send_telegram_report()
