#!/usr/bin/python
# -*- coding: utf-8 -*-
import logging
import time
import os

from common.contentsManage import logDir

# BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
# # 定义日志文件路径
# LOG_PATH = os.path.join(BASE_PATH, "log")
# if not os.path.exists(LOG_PATH):
#     os.mkdir(LOG_PATH)

# 方法1
# 封装自己的logging
class MyLogger:
    def __init__(self):
        self._logName = os.path.join(logDir(), "{}.log".format(time.strftime("%Y%m%d")))
        self._logger = logging.getLogger("logger")
        self._logger.setLevel(logging.DEBUG)
        self._formatter = logging.Formatter('[%(asctime)s][%(filename)s %(lineno)d][%(levelname)s]:%(message)s')
        self._streamHandler = logging.StreamHandler()
        self._fileHandler = logging.FileHandler(self._logName, mode='a', encoding="utf-8")
        self._streamHandler.setFormatter(self._formatter)
        self._fileHandler.setFormatter(self._formatter)
        self._logger.addHandler(self._streamHandler)
        self._logger.addHandler(self._fileHandler)

    # 获取logger日志记录器
    def get_logger(self):
        return self._logger

# 方法二
class LogOutput():
    def logOutput(self, log_dir, log_name):
        now = time.strftime("%Y-%M-%d %H-%M-%s")
        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(messages)s',
                            datefmt='%a,%d %b %Y %H:%M:%S',
                            filename=log_dir + now + '-' + log_name + '_log.txt',
                            filemode='a'
                            )
        logger = logging.getLogger()
        logger.debug('----输出所有用例执行日志----')

logger = MyLogger().get_logger()