#Скрипт, который выполняется при запуске: собирает статику, применяет миграции, запускает сервер.
#!/usr/bin/env bash
python manage.py collectstatic --noinput
python manage.py migrate
gunicorn news.wsgi:application --log-file -