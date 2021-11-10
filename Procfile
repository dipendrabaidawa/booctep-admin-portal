release: python manage.py migrate --no-input
release: python manage.py collectstatic
web: gunicorn admin.wsgi
