import logging
import logging.handlers

import datetime

class debug_logger(object):
	"""docstring for debug_logger"""
	def __init__(self):
		super(debug_logger, self).__init__()
		currentdate = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
		self.logger = logging.getLogger('main')
		self.logger.setLevel(logging.DEBUG)

		debugHandler = logging.handlers.RotatingFileHandler(currentdate+'_debug.log', maxBytes=100, backupCount=5)
		formatter = logging.Formatter('[%(asctime)s/%(name)s/%(levelname)s] %(message)s')
		debugHandler.setFormatter(formatter)
		self.logger.addHandler(debugHandler)

	def print(self, string):		
		self.logger.debug(string)
