import logging

from apscheduler.schedulers.background import BackgroundScheduler

log = logging.getLogger(__name__)


def dummy_task(session):
    log.info('Running dummy task')


def includeme(config):
    session = config.registry['db_sessionmaker']()

    scheduler = BackgroundScheduler()
    scheduler.add_job(dummy_task, 'interval', minutes=1, args=[session])
    scheduler.start()
