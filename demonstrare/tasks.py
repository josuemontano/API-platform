import logging

from apscheduler.schedulers.background import BackgroundScheduler

log = logging.getLogger(__name__)


def dummy_task(session):
    log.info('Running dummy task')


def includeme(config):
    session = config.registry['db_sessionmaker']()

    sched = BackgroundScheduler()
    sched.add_job(dummy_task, 'cron', hour=6, minute=30, args=[session])
    sched.start()
