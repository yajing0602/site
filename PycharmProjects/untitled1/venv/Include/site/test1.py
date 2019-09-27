from locust import HttpLocust, TaskSet, task
import hashlib
import queue
from random import randint
from random import uniform
import time, datetime

class danglaoshi(TaskSet):
    @task(1)
    def login(self):
        url ="http://10.9.17.250:8080/danglaoshi-web-app/user/login"
        headers= {"Content-Type":"application/json;charset=utf-8"}
        data = {"versionName": "3.3.0", "password": "e10adc3949ba59abbe56e057f20f883e", "userName": "13100000123",
                "versionCode": 71, "deviceType": 1}


        with self.client.post(url,data=data,headers=headers,name="登陆") as response:
            if response.status_code == 200:
                response.success()
                print("ok")
            else:
                response.failure('Failed!')


    # @task(2)
    # def queryTaskInfo(self):
    #     url="http://10.9.17.240:12600/api/chili/mystical/queryTaskInfo"
    #     head={"sessionId":"a53d0336-b7b1-497f-bc58-3480f33b4827","source": 1,"userId":"xW1p/SfQrRe="}
    #     with self.client.get(url,headers=head) as response:
    #         if response.status_code == 200:
    #             # response.success()
    #             print("成功")
    #         else:
    #             response.failure('Failed!')
    #             print("失败")
    #
    #             print(response.text)



class WebsiteUser(HttpLocust):
    task_set = danglaoshi
    host=""
    min_wait = 1000
    max_wait = 2000