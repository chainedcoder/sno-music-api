export FLASK_ENV=development
. venv/bin/activate
# flask run -h 0.0.0.0 -p 80
gunicorn --bind 0.0.0.0:8000 wsgi:app