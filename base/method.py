import json
import requests
from common.log import logger
from utils.commonUtils import isJson

class ApiRequest(object):
    # ---- 第一种请求方式封装requests库，调用可根据实际情况传参 ----
    # def send_requests(self, method, url, data=None, params=None, headers=None,
    #                   cookies=None,json=None,files=None,auth=None,timeout=None,
    #                   proxies=None,verify=None,cert=None):
    #     self.res = requestes.request(method=method, url= url, headers=headers,data=data,
    #                                params=params, cookies=cookies,json = json,files=files,
    #                                auth=auth, timeout= timeout, proxies=proxies,verify=verify,
    #                                cert=cert)
    #     return self.res

    # 第二种封装方法
    def get(self, url, data=None, headers=None, payload=None):
        if headers is not None:
            res = requests.get(url=url, data=data,headers=headers)
        else:
            res = requests.get(url=url, data=data)

        return res

    def post(self, url, data, headers, payload:dict, files=None):
        if headers is not None:
            res = requests.post(url=url, data=data, headers=headers)
        else :
            res = requests.post(url=url, data=data)

        if str(res) == "<Response [200]>" :
            return res.json()
        else :
            return res.text

    def put(self,url,data,headers, payload:dict, files=None):
        if headers is not None :
            res = requests.put(url=url,data=data,headers=headers)
        else:
            res = requests.put(url=url,data=data)
        return res

    def delete(self,url,data,headers, payload:dict):
        if headers is not None :
            res = requests.delete(url=url,data=data,headers=headers)
        else:
            res = requests.delete(url=url,data=data)

        return res

    def all_method(self, method, url, data=None, headers=None, payload=None, files=None):
        logger.info(f"请求方法是{method}, 请求地址{url}")
        if headers == None:
            headers = {}

        if method.upper()=='GET':
            res = self.get(url,data,headers, payload)
        elif method.upper()=='POST':
            res = self.post(url, data, headers, payload, files)
        elif method.upper() == 'PUT':
            res = self.put(url, data, headers, payload, files)
        elif method.upper() == 'DELETE':
            res = self.delete(url, data, headers, payload)
        else :
            res = f'请求{method}方式不支持，或者不正确'

        return json.dumps(res, ensure_ascii=False, indent=4, sort_keys=True, separators=(',',':'))