# PhotoAnalyst Bot

**PhotoAnalyst** — это Telegram-бот, который анализирует фотографии и выдает краткий отчет о качестве изображения: резкость, освещённость и рекомендации по улучшению.  
Создан на Python с использованием `aiogram` и `opencv-python`.

---

## Возможности
- Принимает фотографии прямо из чата Telegram  
- Анализирует изображение с помощью OpenCV  
- Определяет:
  - Резкость (на основе дисперсии Лапласиана)
  - Освещённость (по средней яркости)
- Выдает понятный отчёт и советы пользователю  
- Легко разворачивается локально или на сервере (Render / Railway / PythonAnywhere)

---

## Технологии
- Python 3.10+
- [Aiogram](https://docs.aiogram.dev/) — Telegram API
- [OpenCV](https://opencv.org/) — обработка изображений
- [python-dotenv](https://pypi.org/project/python-dotenv/) — конфигурация окружения

---

## Структура проекта
```
photoanalyst_bot/
├── app/
│   ├── __init__.py
│   ├── analyzer.py      # Логика анализа фото
│   ├── bot.py           # Telegram-бот на aiogram
│   ├── config.py        # Загрузка токена из .env
│   └── utils.py         # Вспомогательные функции
├── .env                 # BOT_TOKEN=твой_токен
├── requirements.txt
├── main.py              # Точка входа
└── README.md
```

---

## Установка и запуск

```bash
# 1️. Клонировать репозиторий
git clone https://github.com/KarolDmitriy/photoanalyst_bot.git
cd photoanalyst_bot

# 2️. Создать виртуальное окружение
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/Mac:
source .venv/bin/activate

# 3️. Установить зависимости
pip install -r requirements.txt

# 4️. Создать файл .env в корне проекта
BOT_TOKEN=1234567890:ABCdefGhIjkLmNoPqRsTuvWxYz

# 5️. Запустить бота
python main.py
```

---

## Пример работы

**Пользователь:**  
Отправляет фото  
**Бот:**  
```
Фото получено, анализирую...
Анализ фото:
— Резкость: 4.02/10
— Освещённость: хорошая
Совет: попробуйте немного добавить контраст для улучшения восприятия.
```

---

## Автор
**Кароль Дмитрий Викторович**  
Казахстан → Россия  
Python-разработчик и фотограф  
GitHub: [@KarolDmitriy](https://github.com/KarolDmitriy)

---

## Лицензия
Проект распространяется под лицензией MIT. Используйте свободно с указанием автора.
