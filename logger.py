import logging
import os
from logging.handlers import TimedRotatingFileHandler

from config import Config
from logging_constants import (
    LOG_LEVEL,
    ERROR_LOG_LEVEL,
    LOG_FORMAT,
    DATE_FORMAT,
    LOG_ROTATION_WHEN,
    LOG_ROTATION_INTERVAL,
    LOG_ROTATION_BACKUP_COUNT,
    LOG_SUFFIX_FORMAT,
    LOG_ENCODING,
    LOG_DIR,
    APP_LOG_FILE,
    ERROR_LOG_FILE,
    MAIN_LOGGER_NAME,
    MODULE_LOGGER_PREFIX,
    DEVELOPMENT_MODE,
    PRODUCTION_MODE
)


def setup_logging():
    """Настройка логирования в зависимости от режима"""

    logger = logging.getLogger(MAIN_LOGGER_NAME)
    logger.setLevel(LOG_LEVEL)

    # Очищаем существующие обработчики
    logger.handlers.clear()

    formatter = logging.Formatter(
        LOG_FORMAT,
        datefmt=DATE_FORMAT,
    )

    if Config.SERVERBASE_MODE == PRODUCTION_MODE:
        # PRODUCTION: логи в файлы
        setup_production_logging(logger, formatter)
    else:
        # DEVELOPMENT: логи в консоль
        setup_development_logging(logger, formatter)

    return logger


def setup_production_logging(logger, formatter):
    """Настройка логирования для продакшена"""
    os.makedirs(LOG_DIR, exist_ok=True)

    # Файл для общих логов с ротацией
    file_handler = TimedRotatingFileHandler(
        filename=APP_LOG_FILE,
        when=LOG_ROTATION_WHEN,
        interval=LOG_ROTATION_INTERVAL,
        backupCount=LOG_ROTATION_BACKUP_COUNT,
        encoding=LOG_ENCODING,
    )
    file_handler.setLevel(LOG_LEVEL)
    file_handler.setFormatter(formatter)
    file_handler.suffix = LOG_SUFFIX_FORMAT

    # Файл для ошибок с ротацией
    error_handler = TimedRotatingFileHandler(
        filename=ERROR_LOG_FILE,
        when=LOG_ROTATION_WHEN,
        interval=LOG_ROTATION_INTERVAL,
        backupCount=LOG_ROTATION_BACKUP_COUNT,
        encoding=LOG_ENCODING,
    )
    error_handler.setLevel(ERROR_LOG_LEVEL)
    error_handler.setFormatter(formatter)
    error_handler.suffix = LOG_SUFFIX_FORMAT

    # Консоль для критических ошибок
    console_handler = logging.StreamHandler()
    console_handler.setLevel(ERROR_LOG_LEVEL)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(error_handler)
    logger.addHandler(console_handler)


def setup_development_logging(logger, formatter):
    """Настройка логирования для разработки"""
    console_handler = logging.StreamHandler()
    console_handler.setLevel(LOG_LEVEL)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)


def get_module_logger(module_name):
    """Получить логгер для конкретного модуля"""
    logger = logging.getLogger(f"{MODULE_LOGGER_PREFIX}{module_name}")
    return logger
