"""
下载b站新番时间表并显示
下载页面
"""
import json
import requests

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


def show_page(file_dict):
    # code = file_dict['code']
    message = file_dict['message']
    results = file_dict['result']
    if message == 'success':
        # print(result[0])  #输出成功，说明result确实是一个列表
        for result in results:
            print(result['date'])
            seasons = result['seasons']
            for season in seasons:
                if 'pub_index' in season:
                    print(str(season['pub_time']) + ' ' + str(season['title']) + ' ' + str(season['pub_index']))
                elif 'delay_index' in season:
                    print(str(season['pub_time']) + ' ' + str(season['title']) + ' ' + str(season['delay_index']))
                # 或者 try    except KeyError
        print('\n')


show_page(response_dict)
