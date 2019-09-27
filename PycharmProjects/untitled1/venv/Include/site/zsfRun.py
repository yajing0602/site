from locust import HttpLocust, TaskSet, task ,seq_task
import hashlib
import queue
from random import randint
from random import uniform
import time, datetime
import urllib3



class challenge(TaskSet):
    # def on_start(self):
    #     self.login()
    #
    # #登录
    # def login(self):
    #     url = "https://dls-api-v3.danglaoshi.info/danglaoshi-web-app/user/login"
    #     head ={"Content-Type":"application/json;charset=utf-8"}
    #     datsa ={"deviceType":1,"password":"e10adc3949ba59abbe56e057f20f883e","userName":"13649211017","versionName":"3.3.0","VersionNumber":71}
    #     self.session = "2558c8bb-319e-4ecd-896a-2f5f4d4af9a3"
    #     self.user = "jOf0NnQqZgq="
    #     with self.client.post(url,json=datsa,headers=head,name="登录",catch_response=True)as response:
    #         if response.status_code == 200:
    #             response.success()
    #             print("ok")
    #         else:
    #             response.failure(response.text)

            # if response.json()["code"] == 200:
            #     print("ok")
            #     response.success()
            #     self.user = response.json()["userId"]
            #     print("userId = " + self.user)
            #     self.session = response.json()["sessionId"]
            #     print("sessionId = " + self.session)
            # else:
            #     response.failure(response.text)

    @task (1)
    @seq_task(2)
    # 课程列表
    def list(self):
         # userinfo = self.locust.user_data_queue.get()
        url = "https://dls-api-v3.danglaoshi.info/api/celery/userCourse/list"
        head = {"sessionId":"62a01fe9-ff56-4848-a81f-61ab0505953e","userId":"fwE6pzFQ68I=","Content-Type":"application/json;charset=utf-8"}
        with self.client.get(url,verify=False,headers=head, name="课程列表")as response:
            try:
                urllib3.disable_warnings()
                if response.json()["code"] == 200:
                    # print("课程列表响应信息：",response.text)
                    print ("课程列表ok")
                else:
                    print("课程列表请求出错")
            except  BaseException as error:
                print("课程列表",response.text)
                print("课程列表",error)
            # self.locust.user_data_queue.put_nowait(userinfo)

    @task(1)
    @seq_task(3)
    #课程详情
    def detail(self):
        # userinfo = self.locust.user_data_queue.get()
        url ="https://dls-api-v3.danglaoshi.info/api/celery/userCourse/detail?courseId=1453"
        head ={"sessionId":"62a01fe9-ff56-4848-a81f-61ab0505953e","userId":"fwE6pzFQ68I=","Content-Type":"application/json;charset=utf-8"}
        with self.client.get(url,verify=False,headers=head,name="课程详情") as response:
            try:
                urllib3.disable_warnings()
                if response.json()["code"] == 200:
                    # print("课程详情响应信息：",response.text)
                    print("课程详情ok")
                else:
                    print("课程详情请求出错")
            except  BaseException as error:
                print("课程详情",response.text)
                print("课程详情",error)
            # self.locust.user_data_queue.put_nowait(userinfo)

    @task(1)
    @seq_task(4)
    #课程日历
    def daySchedules(self):
        # userinfo = self.locust.user_data_queue.get()
        url = "https://dls-api-v3.danglaoshi.info/api/celery/userCourse/daySchedules?day=20190905"
        head ={"sessionId":"62a01fe9-ff56-4848-a81f-61ab0505953e","userId":"fwE6pzFQ68I=","Content-Type":"application/json;charset=utf-8"}
        with self.client.get(url,verify=False,headers=head,name="课程日历")as response:
            try:
                urllib3.disable_warnings()
                if response.json()["code"] == 200:
                    print("课程日期ok")
                    # print("课程日历响应信息：",response.text)
                else:
                    print("课程日期请求出错")
            except BaseException as error:
                print("课程日历",response.text)
                print("课程日历",error)

    @task(3)
    @seq_task(5)
    #播放记录
    def playRecord(self):
        # userinfo = self.locust.user_data_queue.get()
        url = "https://dls-api-v3.danglaoshi.info/api/celery/course/playRecord"
        head ={"sessionId":"62a01fe9-ff56-4848-a81f-61ab0505953e","userId":"fwE6pzFQ68I=","Content-Type":"application/json;charset=utf-8","source":"1"}
        datas={}
        with self.client.post(url,verify=False,headers=head,json=datas,name="播放记录") as response:
            try:
                urllib3.disable_warnings()
                if response.json()["code"] == 200:
                    print("播放记录响应信息：",response.text)
                    print("播放记录ok")
                else:
                    print("播放记录请求出错")
                    print("播放记录", response.text)
            except  BaseException as error:
                print("播放记录",response.text)
                print("播放记录",error)
            # self.locust.user_data_queue.put_nowait(userinfo)

    @task(1)
    @seq_task(6)
    # 今日课程
    def todayCourse(self):
        # userinfo = self.locust.user_data_queue.get()
        url = "https://dls-api-v3.danglaoshi.info/api/celery/userCourse/daySchedules?day=20190905"
        head = {"sessionId":"62a01fe9-ff56-4848-a81f-61ab0505953e","userId":"fwE6pzFQ68I="}
        with self.client.get(url,verify=False,headers=head,name="今日课程") as response:
            try:
                urllib3.disable_warnings()
                if response.json()["code"] == 200:
                    # response.success()
                    # print("今日课程响应信息：",response.text)
                    print("今日课程ok")
                else:
                    print("今日课程请求出错")
            except  BaseException as error:
                print("今日课程",response.text)
                print("今日课程",error)
            # self.locust.user_data_queue.put_nowait(userinfo)

    @task (1)
    @seq_task(7)
    # 进入教室
    def todayCourse(self):
        # userinfo = self.locust.user_data_queue.get()
        url = "https://dls-api-v3.danglaoshi.info/api/celery/listeningCourse/getConfig?courseScheduleId=29793&courseId=1331"
        head = {"sessionId":"62a01fe9-ff56-4848-a81f-61ab0505953e","userId":"fwE6pzFQ68I=","source":"1"}
        with self.client.get(url,verify=False,headers=head,name="进入教室") as response:
            try:
                urllib3.disable_warnings()
                if response.json()["code"] == 200:
                    # print("点击课时：",response.text)
                    print ("进入教室ok")
                else:
                    print("进入教室请求出错")
                    print("点击课时：", response.text)
            except  BaseException as error:
                print("点击课时",response.text)
                print("点击课时",error)
        # self.locust.user_data_queue.put_nowait(userinfo)


class WebsiteUser(HttpLocust):
    task_set = challenge
    host = ""
    min_wait = 1000
    max_wait = 4000
