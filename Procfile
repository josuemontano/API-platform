web: poetry run gunicorn --paste $APP_CONFIG_FILE
worker: poetry run huey_consumer.py canopus.tasks.huey -w 2