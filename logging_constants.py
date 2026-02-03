"""
Константы для настройки системы логирования
"""

import os

# Уровни логирования
LOG_LEVEL = "INFO"
ERROR_LOG_LEVEL = "ERROR"

# Форматирование
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

# Настройки ротации логов
LOG_ROTATION_WHEN = "D"  # Дни
LOG_ROTATION_INTERVAL = 3  # Каждые 3 дня
LOG_ROTATION_BACKUP_COUNT = 10  # Хранить 10 файлов
LOG_SUFFIX_FORMAT = "%Y-%m-%d"  # Формат даты в имени файла
LOG_ENCODING = "utf-8"

# Пути к лог-файлам
LOG_DIR = "/opt/foresight/mail-orchestrator/logs"
APP_LOG_FILE = os.path.join(LOG_DIR, "app.log")
ERROR_LOG_FILE = os.path.join(LOG_DIR, "error.log")

# Имена логгеров
MAIN_LOGGER_NAME = "app"
MODULE_LOGGER_PREFIX = "app."

# Режимы работы
DEVELOPMENT_MODE = "DEVELOPMENT"
PRODUCTION_MODE = "WSGI"
