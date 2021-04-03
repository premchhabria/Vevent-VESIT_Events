web: gunicorn eventWebsite.wsgi:application --log-file - --log-level debug
python manage.py collectstatic --noinput
release: python manage.py makemigrations vesitEvents
release: python manage.py migrate vesitEvents
