import logging

import requests
from requests.exceptions import ConnectionError, Timeout

log = logging.getLogger(__name__)


class MailNotifier(object):
    url = None
    api_key = None
    sender = None

    @classmethod
    def send_message(cls, subject, to, message):
        data = {'from': cls.sender, 'to': to, 'subject': subject, 'html': message}
        try:
            requests.post(cls.url, auth=('api', cls.api_key), data=data, timeout=5)
        except (ConnectionError, Timeout):
            log.error('Failed to deliver message %s', data)


def includeme(config):
    """
    Sets the mailgun properties from .ini config file

    :param config: The pyramid ``Configurator`` object for your app.
    :type config: ``pyramid.config.Configurator``
    """
    settings = config.get_settings()

    MailNotifier.url = settings['mailgun.url']
    MailNotifier.api_key = settings['mailgun.key']
    MailNotifier.sender = settings['mailgun.sender']
