import logging
import coloredlogs

logger = logging.getLogger("order_test_logger")
logger.setLevel(logging.DEBUG)

coloredlogs.install(level='DEBUG', logger=logger, fmt='%(asctime)s [%(levelname)s] %(message)s')
