from visa.logger import logging
from visa.exception import visaException
import sys


logging.info("hi")


try:
    a = 2/0
except Exception as e:
    raise visaException(e, sys)