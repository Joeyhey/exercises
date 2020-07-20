import json
import pygal_maps_world.maps
from country_codes import get_country_code
from pygal.style import RotateStyle, LightColorizedStyle

# 将数据加载到一个列表中
filename = 'gdp_json.json'
with open(filename) as file_obj:
    gdp_data = json.load(file_obj)

# 创建一个包含gdp的字典
cc_gdps = {}
for gdp_dict in gdp_data:
    if gdp_dict['Year'] == 2016:
        country_name = gdp_dict['Country Name']
        gdp = int(float(gdp_dict['Value']))
        code = get_country_code(country_name)
        if code:
            # print(code + ": " + str(gdp))
            cc_gdps[code] = gdp
        else:
            print("ERROR - " + country_name)
            # pass

# print(len(cc_gdps))

wm_style = RotateStyle('#226699', base_style=LightColorizedStyle)
wm = pygal_maps_world.maps.World(style=wm_style)
wm.title = "World GDP in 2016, by country"
wm.add('2016', cc_gdps)

wm.render_to_file("D:\Project\exercises\worldwide_gdp\world_gdp.svg")