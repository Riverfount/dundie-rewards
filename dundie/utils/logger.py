import logging
import os
from logging import handlers

LOG_LEVEL = os.getenv('LOG_LEVEL', 'WARNING').upper()
log = logging.getLogger('dundie')
fmt = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s '
    'l:%(lineno)d f:%(filename)s: %(message)s'
)


def get_logger(log_file='dundie.log'):
    """Returns a configures logger."""
    fh = handlers.RotatingFileHandler(
        log_file,
        maxBytes=1024 * 100,
        backupCount=3,
    )
    fh.setLevel(LOG_LEVEL)
    fh.setFormatter(fmt)
    log.addHandler(fh)
    return log
