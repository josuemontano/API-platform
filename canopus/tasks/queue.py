import os

from huey import RedisHuey
from pyramid.paster import get_appsettings


redis_url = os.environ.get('REDIS_URL', 'redis://127.0.0.1:6379/9')
paster_config = get_appsettings(os.environ.get('APP_CONFIG_FILE', 'development.ini'))
huey = RedisHuey('canopus', url=redis_url)
