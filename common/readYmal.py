import yaml
from common.log import logger
from common.contentsManage import filePath


class ReadYaml:
    @staticmethod
    def read(path):
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = yaml.safe_load(f)
                return data
        except Exception as e:
            logger.exception(f"请查看文件是否正确，异常信息是{str(e)}")
            return None


if __name__ == "__main__":
    print(filePath(fileName="test_login.yml"))
    print(ReadYaml.read(filePath(fileName="test_login.yml")))