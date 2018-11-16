#coding=utf-8

import datetime

d1 = datetime.datetime.now()
d2 = datetime.datetime(2020,4,20)
d3 = (d2-d1).days

print(d3)
