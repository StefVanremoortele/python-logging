import os
import yaml
import logging
import logging.config

# load my module
import my_module

# init logging config
my_module.setup_logging()


my_module.foo()

bar = my_module.Bar()
bar.bar()
bar.barError()

logger = logging.getLogger(__name__)
logger.info('Some random info message from main.py')

try:
    open('/path/to/does/not/exist', 'rb')
except (SystemExit, KeyboardInterrupt):
    raise
except Exception as e:
    logger.error('Failed to open file', exc_info=True)


logger.debug('Debugging something in main')