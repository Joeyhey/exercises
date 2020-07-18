# 展示国别码，对程序没什么用？
from pygal_maps_world.i18n import COUNTRIES
for country_code in sorted(COUNTRIES.keys()):
    print(country_code, COUNTRIES[country_code])