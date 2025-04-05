from model.train_model import train_model
import time

if __name__ == "__main__":
    train_model()
    while True:
        time.sleep(3600)  # спим 1 час, чтобы Render не рестартовал процесс
