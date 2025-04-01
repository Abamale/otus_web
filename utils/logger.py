import logging
import os


LOG_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "logs"))
os.makedirs(LOG_DIR, exist_ok=True)
LOG_FILE = os.path.join(LOG_DIR, "test_log.log")

def setup_logger(name="TestLogger"):
    """Создание и настройка глобального логгера"""
    logger = logging.getLogger(name)
    if logger.hasHandlers():
        return logger  # Если логгер уже настроен, не создаём новый

    logger.setLevel(logging.INFO)

    # Обработчик для записи в файл
    file_handler = logging.FileHandler(LOG_FILE, encoding="utf-8")
    file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(file_formatter)

    # Обработчик для вывода в консоль
    console_handler = logging.StreamHandler()
    console_formatter = logging.Formatter("%(levelname)s: %(message)s")
    console_handler.setFormatter(console_formatter)

    # Добавляем обработчики к логгеру
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

# Глобальный логгер
logger = setup_logger()