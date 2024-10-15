from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    # Получаем текущие дату и время
    now = datetime.now()
    # Форматируем дату и время в строку
    formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
    # Возвращаем HTML-код с отображением даты и времени
    return f"<h1>Current date and time:</h1><p>{formatted_time}</p>"

if __name__ == '__main__':
    app.run()