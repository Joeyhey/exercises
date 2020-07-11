"""
下载b站新番时间表并显示
下载页面
"""
import json
import requests
from show import show_page  # 这是pycharm觉得show不在根目录，但是实际上是对的，忽略之


# 调用API并存储响应
url = 'https://bangumi.bilibili.com/web_api/timeline_global'
r = requests.get(url)
# print("Status code: ", r.status_code)

# 将API响应存储在一个变量里面
response_dict = r.json()

filename = 'bilibili_schedule.json'
with open(filename, 'w') as file_object:
    json.dump(response_dict, file_object, indent=4)  # ndent=4 写成pprint那个样子
    # response_dict = json.load(file_object)

show_page(response_dict)
