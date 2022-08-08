"""Core module of dundie. """
from dundie.utils.logger import get_logger

log = get_logger()


def load(filepath):
    """Loads data from filepath to the database."""
    try:
        with open(filepath) as f:
            return [line.strip() for line in f.readlines()]
    except FileExistsError as e:
        log.error(str(e))
        raise e
