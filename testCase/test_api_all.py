# 参数化运用所有用例
import json
import pytest

from utils.operationExcel import OperationExcel, ExcelVarles
from base.method import ApiRequest
from common.log import logger

opExcel = OperationExcel()
apiRequest = ApiRequest()

@pytest.mark.parametrize('data', opExcel.getExcelData()) # 装饰器进行封装用例
def test_api(data, login_token=None):
    if data[ExcelVarles.case_isRun] == "N" :
        logger.info("跳过执行用例")
        return

    # 请求头作为空处理并添加token
    headers = data[ExcelVarles.case_headers]
    if len(str(headers).split()) == 0:
        pass
    elif len(str(headers).split()) >= 0:
        headers = json.loads(headers) # 转换为字典
    #     headers['Authorization'] = login_token # 获取登录返回的token并添加到读取出来的headers里面
        headers = headers

    # 对请求参数做为空处理
    params = data[ExcelVarles.case_data]
    if len(str(params).split()) == 0:
        pass
    elif len(str(params).split()) == 0:
        params = params

    url = data[ExcelVarles.case_server] + data[ExcelVarles.case_url] + "?" + params
    r = apiRequest.all_method( data[ExcelVarles.case_method] ,url, headers=headers)
    logger.info(f"响应结果{r}")
    responseResult = json.loads(r)

    case_result_assert(data[ExcelVarles.case_code], responseResult['code'])

# 断言封装
def case_result_assert(expectedResult, actualReuls) :
    '''
    断言封装
    :param expectedResult: 预期结果
    :param actualReuls: 实际结果
    :return:
    '''
    assert expectedResult == actualReuls # 状态码