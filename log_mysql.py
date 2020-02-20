import logging
from logging.handlers import TimedRotatingFileHandler

class MyLog():
    def __init__(self, name, filename):
        self.logger = logging.getLogger(name)
        if not self.logger.handlers:
            self.logger.setLevel(logging.INFO)
            ch = TimedRotatingFileHandler(filename=filename, when='midnight', encoding="utf-8")
            ch.setLevel(logging.DEBUG)
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            ch.setFormatter(formatter)
            self.logger.addHandler(ch)


'''
logger = MyLog("test","log\\text.txt")
logger.logger.debug('debug message')
logger.logger.info('info message')
logger.logger.warning('warn message')
logger.logger.error('error message')
logger.logger.critical('critical message')
'''


