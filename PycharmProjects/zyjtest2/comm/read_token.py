import yaml
import os

cur = os.path.dirname(os.path.dirname(os.path.realpath(__file__))) #获取上一级目录


def get_token(yamlName="config.yaml"):
    '''
    从config.yaml读取token值
    :param yamlName: 配置文件名称
    :return: token值
    '''
    p = os.path.join(cur,"config",yamlName)
    f = open(p)
    a = f.read()
    t = yaml.load(a)
    f.close()
    return t["token"]

#
# if __name__ =="__main__":
#     print(get_token())