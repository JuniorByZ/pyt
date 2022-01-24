import logging
import logging.config

logging.config.fileConfig('logging.conf')


logger = logging.getLogger('simpleExample')
logger.debug("Debug Message !...")

""" # create handler
stream_h = logging.StreamHandler()
file_h = logging.FileHandler('file.log')

# level and the format
stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

formatter = logging.Formatter('%(name)s - %(level)s - %(message)s')
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

logger.addHandler(stream_h)
logger.addHandler(file_h)

logger.warning('This is a Warning !...')
logger.error('This is a Error !...') """
