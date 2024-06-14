import json
import logging
import os
from typing import List, Dict

# Создаем директорию logs, если она не существует
os.makedirs('logs', exist_ok=True)

# Настройка логера
logger = logging.getLogger(__name__)
handler = logging.FileHandler('logs/utils.log', mode='w')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)


def read_json_file(filepath: str) -> List[Dict]:
    """Чтение данных из JSON-файла и возврат списка словарей с транзакциями."""
    logger.info(f'Чтение файла: {filepath}')
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            data = json.load(file)
            if isinstance(data, list):
                logger.info(f'Успешное чтение файла: {filepath}')
                return data
            else:
                logger.warning(f'Файл {filepath} не содержит список.')
                return []
    except FileNotFoundError:
        logger.error(f'Файл {filepath} не найден.')
        return []
    except json.JSONDecodeError:
        logger.error(f'Ошибка декодирования JSON в файле {filepath}.')
        return []
