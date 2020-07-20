# 定义获取国别码的函数，该国别码能被pygal识别
from pygal_maps_world.i18n import COUNTRIES
import json


def get_country_code(country_name):
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code

    # 如果没有找到指定的国家，就返回None
    return None

# if __name__ == '__main__':
#     filename = 'gdp_json.json'
#     with open(filename) as f:
#         data = json.load(f)
#
#     for dic in data:
#         for key in dic:
#             if key == 'Year':
#                 if dic[key] == 2016:
#                     country_name = dic['Country Name']
#                     print(country_name + ": " + str(get_country_code(country_name)))