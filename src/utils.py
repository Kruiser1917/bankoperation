import json
import logging

# Настройка логирования для модуля utils
logger = logging.getLogger(__name__)
handler = logging.FileHandler('logs/utils.log', mode='w')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.ERROR)

def read_json(file_path):
    """
    Читает JSON-файл и возвращает данные в виде списка словарей.
    Если файл пуст, не найден или содержит некорректные данные,
    возвращается пустой список.

    :param file_path: Путь к JSON-файлу
    :return: Список словарей с данными или пустой список
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            else:
                logger.error("JSON data is not a list")
                return []
    except FileNotFoundError:
        logger.error(f"File not found: {file_path}")
        return []
    except json.JSONDecodeError:
        logger.error("Failed to decode JSON")
        return []

# Добавьте другие функции модуля utils, если они есть, с соответствующей настройкой логирования
