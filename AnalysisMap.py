from pyecharts import Style#为了简化配置项编写，提供了一个 Style 类，可用于在同一个图或者多个图内保持统一的风格
from pyecharts import Geo#直角坐标系上的散点图可以用来展现数据的 x，y 之间的关系，如果数据项有多个维度，可以用颜色来表现，利用 geo 组件

#读取城市数据
city = []
with open('xie_zheng_result.txt', 'r', encoding='utf-8') as f:
    rows = f.readlines()
    for row in rows:
        if len(row.split(',')) == 5 and row.split(',')[2] != '':#抓取的一些城市名为空,去掉
            #cityname = row.split(',')[2].replace('\n', '')
            cityname = row.split(',')[2]
            city.append(cityname)

#统计评论中个城市出现的次数
def all_list(arr):
    result = {}
    for i in set(arr):#使用set去重
        result[i] = arr.count(i)#城市名：出现次数
    return result


data = []
for item in all_list(city):
    # append 只能添加一个参数，双括号代表添加的是元组
    data.append((item, all_list(city)[item]))

style = Style(
    title_color='#fff',
    title_pos='center',
    width=1200,
    height=600,
    background_color='#404a59'
)
geo = Geo('<邪不压正>粉丝人群地理位置', '数据来源：猫眼', **style.init_style)
# 属性，值
attr, value = geo.cast(data)
geo.add("", attr, value, visual_range=[0, 20],
        visual_text_color="#fff", symbol_size=10,
        is_visualmap=True, is_piecewise=True
        #visual_split_number=4
        )
geo.render('邪不压正粉丝人群地理位置.html')
