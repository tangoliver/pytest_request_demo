import shutil
import pytest
import os

from common.log import logger
import subprocess # 通过标准库中的subprocess包来fork一个子进程,并运行一个外部的程序
from common.contentsManage import htmlDir, resultDir

if __name__ == '__main__':
    htmlPath = htmlDir()
    resultPath = resultDir()
    if os.path.exists(resultPath) and os.path.isdir(resultPath):
        logger.info("清理上一次执行的结果")
        shutil.rmtree(resultPath, True)

    logger.info("开始测试")
    pytest.main(["-s", "-v", "--alluredir", resultPath]) #运行输出并在resport/result目录下生成json文件
    logger.info("结束测试")

    # 如果是代码单独执行，需要立马看到报告，可以执行下面语句，如果配合Jenkins使用，则可以不需要执行，Jenkins自带的插件allure会操作
    # logger.info("生成报告")
    # subprocess.call('allure generate ' + resultPath + ' -o '+ htmlPath +' --clean', shell=True) # 读取json文件并生成html报告,--clean诺目录存在则先清楚
    # logger.info("查看报告")
    # subprocess.call('allure open -h 127.0.0.1 -p 9999 '+htmlPath+'', shell=True) #生成一个本地的服务并自动打开html报告
