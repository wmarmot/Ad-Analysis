#!/usr/bin/env python
# coding=utf-8
# author:marmot

import pandas as pd
from adjust_price import set_float_value

initdata=pd.read_excel(unicode(r"D:\待处理\KIMISS_FR\report\123.xlsx"))

base_path11=r".\base_acos_float\atuo_float_bid_base_acos.xlsx"
base_path22=r".\base_acos_float\atuo_float_bid_base_click.xlsx"
acos_list = [0, 3, 5, 8, 10, 14, 20, 25, 30, 35, 40, 10000000]
click_list = [0, 3, 5, 10, 15, 20, 25, 30, 40, 50]

#set_float_value(base_path1,base_path2, dataframe, sectionlist1, sectionlist2, flagname1,flagname2)
#添加差值
initdata=set_float_value(base_path11, base_path22,initdata, acos_list, click_list, 'acos_abbr','click_abbr')
print initdata[u'差值']
initdata.to_excel(unicode(r"D:\待处理\KIMISS_FR\report\123.xlsx"),sheet_name='123',na_rep='',index=False)
