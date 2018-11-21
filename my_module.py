import yaml
import logging
import logging.config
import coloredlogs
import os

def setup_logging(
    default_path='logger_config.yaml',
    default_level=logging.INFO,
    env_key='LOG_CFG'
):
    """Setup logging configuration"""
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
        coloredlogs.install()

    else:
        logging.basicConfig(level=default_level)

def foo():
    logger = logging.getLogger(__name__)
    logger.info('Hi, foo')

class Bar(object):
    def __init__(self, logger=None):
        self.logger = logger or logging.getLogger(__name__)

    def bar(self):
        self.logger.info('Hi, bar')

    def barError(self):
        self.logger.error("Hi, bar. I'm afraid there's an error")