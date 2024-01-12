import json.decoder
import os
def isJson(json_str):
    '''
    :判断字符串是否为json格式
    :param json_str: 字符串
    :return: bool
    '''
    try:
        json_str.loads()
        return True
    except ValueError:
        return False


def isDir(dir_str) :
    '''
    :判断是否为目录
    :param dir_str: 目录
    :return: bool
    '''
    if os.path.isdir(dir_str) :
        return True
    else :
        return False

def isFileExists(file_str):
    '''
    : 判断文件是否存在
    :param file_str:
    :return: bool
    '''
    if os.path.exists(file_str):
        return True
    else :
        return False