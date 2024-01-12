import os

# cur_path = os.path.dirname(__file__) #获取当前目录
# parent_path = os.path.dirname(cur_path) #获取当前目录的上一级目录

def projectDir():
    '''
    项目目录
    :return:返回
    '''
    base_path = os.path.dirname(os.path.dirname(__file__))
    return os.path.join(base_path).replace("\\", "/")

def logDir():
    '''
    log目录
    :return:返回
    '''
    # log_path = projectDir() + "/log"
    return os.path.join(projectDir() + "/log")

def reportsDir():
    '''
    :报告目录
    :return: 返回
    '''
    # reports_path = projectDir() + "/reports"
    return os.path.join(projectDir() + "/reports") #将获取到的目录返回

def htmlDir():
    '''
    : 生成的html报告目录
    :return:返回
    '''
    # html_path = reportsDir() + "/html"
    return os.path.join(reportsDir() + "/html")

def resultDir():
    '''
    : 执行结果
    :return:  放回
    '''
    return os.path.join(reportsDir() + "/results")

def configDir():
    '''
    : 配置文件
    :return: 返回
    '''
    # config_path = projectDir() + "/config"
    return os.path.join(projectDir() + "/config")

def filePath(fileDir="testData",fileName="data.xlsx"):
    '''
    :param fileDir: 文件夹
    :param fileName: 文件名称
    :return: 返回
    '''

    test_case_file = projectDir() + "/" + fileDir
    return os.path.join(test_case_file, fileName).replace("\\", "/")

if __name__ == '__main__':
    print(projectDir() + "\n" + logDir() + "\n" + reportsDir())
    print(filePath())