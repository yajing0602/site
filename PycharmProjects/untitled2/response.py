import requests

url = "http://10.9.17.240:12600/api/celery/courseSchedule/list?courseId=2812"
header ={"Content-Type": "application/json","sessionId":"f1213e01-e282-4df8-949c-1af2394c5a7a","userOrgId":"n/gVxHpel5q="}
response=requests.get(url,headers=header)
print(response.text)       #{"msg":"success","code":200,"data":[{"id":41682,"name":"1","startTime":1569393605000,"endTime":1569396606000,"teacherName":"","scene":1,"place":"","isTrial":0,"raiseHands":0,"description":"","createTime":1569393020046,"showScheduleTime":true,"courseScheduleSupportId":41915,"liveStatus":0,"isShowRedFlower":0},{"id":41680,"name":"11","startTime":1569479377000,"endTime":1569482979000,"teacherName":"","scene":1,"place":"","isTrial":0,"raiseHands":0,"description":"","createTime":1569393010677,"showScheduleTime":true,"courseScheduleSupportId":41913,"liveStatus":0,"isShowRedFlower":0},{"id":41681,"name":"11","startTime":1569479737000,"endTime":1569482979000,"teacherName":"","scene":1,"place":"","isTrial":0,"raiseHands":0,"description":"","createTime":1569393010682,"showScheduleTime":true,"courseScheduleSupportId":41914,"liveStatus":0,"isShowRedFlower":0},{"id":41679,"name":"11","startTime":1569479737000,"endTime":1569482979000,"teacherName":"","scene":1,"place":"","isTrial":0,"raiseHands":0,"description":"","createTime":1569393010675,"showScheduleTime":true,"courseScheduleSupportId":41912,"liveStatus":0,"isShowRedFlower":0}],"timestamp":1569562479116}
print(type(response.text)) # str
print(response.content)
print(type(response.content))