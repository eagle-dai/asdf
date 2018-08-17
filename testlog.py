import logging
from logging.config import fileConfig
import utils

fileConfig(utils.resource_path('conf', 'log.conf'))
logger = logging.getLogger()
logger.debug('this is a logger debug message')
logger.info('this is a logger info message')
logger.warning('this is a logger warning message')
logger.error('this is a logger error message')
logger.critical('this is a logger critical message　好的呢')
utils.test_log()