import json

from common.contentsManage import filePath
import xlrd, xlwt
class OperationExcel:
    # 获取shell表
    def getSheet(self, index=0):
        book = xlrd.open_workbook(filePath())
        return book.sheet_by_index(index) #根据索引获取到sheet表

    # 以列表形式读取出所有数据
    def getExcelData(self, index=0):
        data = []
        sheet = self.getSheet(index=index)
        title = sheet.row_values(0) # (0)获取第一行也就是表头
        for row in range(1, sheet.nrows): # 从第二行开始获取
            row_value = sheet.row_values(row)
            data.append(dict(zip(title, row_value))) # 将读取出第一条用例作为一个字典存放近列表

        return data

    def writeExcelData(self, col, row, text):
        '''
        excel坐标从（0,0）开始
        :param col:行坐标
        :param row:纵坐标
        :param text: 内容
        :return:
        '''
        file = filePath(fileName="result.xlsx")
        data = self.getExcelData()
        # print(f"{data}")
        data = str(data).replace("'", "\"").replace("\\\\", "\\")
        # print(f"{data}")
        # json_data = json.load(data)
        json_data = json.loads(data)
        # print(type(json_data))
        # 1. 创建Excel表对象（encoding='utf8'可不写）
        workbook = xlwt.Workbook(encoding='utf8')
        # 2. 新建sheet表（Sheet1为表格名称）
        sheet = workbook.add_sheet('Sheet1')
        row_index = 1  #行
        for item in json_data:
            col_index = 1  #列
            for key,value in item.items():
                if row_index == 1:
                    sheet.write(row_index, col_index, key)
                sheet.write(row_index + 1, col_index, value)
                col_index +=1

            row_index += 1

        # 3. 保存文件分两种格式
        # workbook.save('test.xls')
        workbook.save(file)

# 对excel表头进行全局变量定义
class ExcelVarles:
    case_Id = "用例ID"
    case_module="用例模块"
    case_name="用例名称"
    case_server="用例地址"
    case_url="请求地址"
    case_method="请求方法"
    case_type="请求类型"
    case_data="请求参数"
    case_headers="请求头"
    case_preposition="前置条件"
    case_isRun = "是否执行"
    case_code = "状态码"
    case_result = "期望结果"

if __name__ == "__main__":
    opExcel = OperationExcel()
    # opExcel.getSheet()
    # print(opExcel.getExcelData())

    opExcel.writeExcelData(1, 7, f"test{2}")

