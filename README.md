# Nginx Log Analyzer

Анализатор логов nginx для формирования статистического отчета.

## Установка

1. Установите Poetry:
   ```bash
   pip install poetry
   ```

2. Установите зависимости:
   ```bash
   poetry install
   ```

## Использование

Запустите анализатор:
poetry run python -m nginx_log_analyzer.cli --logfile logs/access.log

## Тестирование

poetry run pytest

## Лицензия

MIT