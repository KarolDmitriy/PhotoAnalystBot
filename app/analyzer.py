import cv2
import numpy as np
from io import BytesIO
import requests

async def analyze_image(bot, file_path: str) -> str:
    # Скачиваем фото
    file_url = f"https://api.telegram.org/file/bot{bot.token}/{file_path}"
    response = requests.get(file_url)
    img_array = np.asarray(bytearray(response.content), dtype=np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

    # Анализ резкости (по Лапласу)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    variance = cv2.Laplacian(gray, cv2.CV_64F).var()
    sharpness_score = round(min(variance / 100, 10), 2)

    # Анализ освещения
    brightness = np.mean(gray)
    light = "тёмная" if brightness < 90 else "светлая" if brightness > 180 else "хорошая"

    return (
        f"Анализ фото:\n"
        f"— Резкость: {sharpness_score}/10\n"
        f"— Освещённость: {light}\n"
        f"Совет: попробуйте немного {'осветлить' if light == 'тёмная' else 'уменьшить яркость' if light == 'светлая' else 'добавить контраст'} для улучшения восприятия."
    )
