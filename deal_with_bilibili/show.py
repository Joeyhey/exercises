"""展示规范"""
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
