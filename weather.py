# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 08:48:43 2020

@author: 10437
"""
import pandas as pd
import numpy as np
from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.faker import Faker
import os
from pyecharts.components import Table
from pyecharts.options import ComponentTitleOpts

province = "jiangsu"
city = "无锡"
District = "惠山"
url = r'http://www.weather.com.cn/textFC/%s.shtml' % province

data = pd.read_html(url)

temp = []
date = []
for i in data:
    if (len(i.index) == 2):
        temp.append(i.iloc[0, 0:8])
        date.append(i.iloc[0, 2])
        temp.append(i.iloc[1, 0:8])
    else:
        if (i.loc[0, 0] == "%s" % city):
            for j in range(len(i.index)):
                temp.append(i.iloc[j, 0:8])
temp2 = pd.DataFrame(temp)

temp3 = []
for i in range(len(temp2.index)):
    if (temp2.iloc[i, 1] == "%s" % District):
        temp3.append(temp2.iloc[i, 2:8])

temp4 = pd.DataFrame(temp3)

temp4.index = date
temp4.columns = temp2.iloc[1, 2:8].tolist()

table = Table()
headers = ["日期", "白天天气", "白天风力", "最高气温", "晚上天气", "晚上风力", "最低气温"]

rows = []
for n in range(len(temp4.index)):
    rows.append([temp4.index[n]] + temp4.iloc[n, :].tolist())

table.add(headers, rows)
table.set_global_opts(
    title_opts=ComponentTitleOpts(title="路边社天气预报：%s-%s" % (city, District), subtitle="商务合作请联系：1043768077@qq.com", )
)

table.render("table_base.html")
os.system('"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" table_base.html')


