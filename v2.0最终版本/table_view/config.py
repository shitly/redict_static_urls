"""
    配置文件: 为了更好的使用本脚本而服务的配置文件
"""
STATIC_ROOT = "F:\\beifen\\net_beifen_0630\\3g.roothan.com\\wxb726\\static\\wxb726\\"

# 主要是 URL 和 View 中的替换
APP_NAME = "wxb726"

# 需要修改的位置  rewrite_htmls 66-67行的 Echarts 配置
ECHARTS = "/static/wxb1/gk/js/echartmap/echarts"

ECHARTS_MAP = "/static/wxb1/gk/js/echartmap/map"

import os 

file_lists = ["../py_data", "../data", "../"+APP_NAME]

for file in file_lists:
    try: 
        os.mkdir(file)
    except:
        pass 
# 需要修改的位置  rewrite_htmls 66-67行的 Echarts 配置

"""
    现在出现的问题; 存在多个规则在第一行的情况。 首页有问题。需要修改首页的配置情况。
"""