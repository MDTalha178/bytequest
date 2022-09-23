web: gunicorn bytequestassignment.wsgi
release: python manage.py makemigrations --noinputs
release: python manage.py collectstatic --noinputs
release: python manage.py migrate
