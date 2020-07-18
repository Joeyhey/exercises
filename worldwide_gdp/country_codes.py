# 定义获取国别码的函数，该国别码能被pygal识别
from pygal_maps_world.i18n import COUNTRIES


def get_country_code(country_name):
    for code, name in COUNTRIES.items():
        if country_name == name:
            return code

    # 如果没有找到指定的国家，就返回None
    return None
