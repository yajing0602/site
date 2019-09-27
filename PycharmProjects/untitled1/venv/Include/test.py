from locust import HttpLocust, TaskSet, task
# import hashlib
# import queue
# from random import randint
# from random import uniform
# import time, datetime

class challenge(TaskSet):
    @task(1)
    # 登录
    def login(self):
        url = "http://10.9.17.250:8080/danglaoshi-web-app/user/login"
        head = {"Content-Type": "application/json;charset=utf-8"}
        data = {"versionName": "3.3.0", "password": "e10adc3949ba59abbe56e057f20f883e", "userName": "13100000123",
                "versionCode": 71, "deviceType": 1}
        response = self.client.post(url, data=data, headers=head,name="登录")

    @task(2)
    #商品列表
    def login(self):
        url = "http://10.9.17.250:8080/api/chili/goods/goodsList"
        head ={"Content-Type":"application/json;charset=utf-8","sessionId":"3c0317af-1361-4bcd-be43-6f2c52446368","userId":"cKttZekd4Oe="}
        datsa ={"categoryId":1}
        with self.client.post(url,json=datsa,headers=head,name="课程列表")as response:
            if response.status_code == 200:
                response.success()
                print("ok")

            else:
                response.failure('Failed!')

#
#     @task(2)
#     #商品详情
#     def detail(self):
#         url = "api/chili/goodsDetail/detail?goodsId=2352 "
#         head ={"Content-Type":"application/json;charset=utf-8","sessionId":"3c0317af-1361-4bcd-be43-6f2c52446368","userId":"cKttZekd4Oe="}
#         datsa ={}
#         with self.client.post(url,json=datsa,headers=head,name="商品详情")as response:
#             if response.status_code == 200:
#                 response.success()
#                 print("ok")
#
#             else:
#                 response.failure('Failed!')
# # class challenge(TaskSet):
#     @task(2)
#     #课程tab
#     def login(self):
#         url = "/api/chili/goods/categorys"
#         head ={"Content-Type":"application/json;charset=utf-8","sessionId":"3c0317af-1361-4bcd-be43-6f2c52446368","userId":"cKttZekd4Oe="}
#         datsa ={}
#         with self.client.post(url,json=datsa,headers=head,name="课程tab")as response:
#             if response.status_code == 200:
#                 response.success()
#                 print("ok")
#
#             else:
#                 response.failure('Failed!')


# class challenge(TaskSet):
#     @task(1)
#     #登录
#     def login(self):
#         url="http://10.9.17.250:8080/danglaoshi-web-app/user/login"
#         head={"Content-Type": "application/json;charset=utf-8"}
#         data={"versionName":"3.3.0","password":"e10adc3949ba59abbe56e057f20f883e","userName":"13100000123","versionCode":71,"deviceType":1}
#         response=self.client.post(url,data=data,headers=head)



class Discuz_Locust(HttpLocust):
    task_set = challenge
    host = ""
    min_wait = 1000
    max_wait = 2000