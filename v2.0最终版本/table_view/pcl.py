import pandas as pd 
import numpy as np
import re

import os
from os.path import join, dirname, abspath
DIR = dirname(dirname(abspath(__file__)))

import sys
sys.path.insert(0, DIR)
from config import APP_NAME
"""
*********************** Django 模板 URL 和 View 设置 ********************************
html 重定向模板修改和替换。 第三个环节。 规则 -> 整理 ->重定向(第三个环节)
URL 设置; 所有的静态文件 原始路径 + url 设置规则 ==> 新的 URL/重定向/ == view的名字
************* APP 名字统一为 appo **************************************************
************************************************************************************
"""
## 这里只会涉及到 html 和模板 也就是 表1
def url_config():
    from table_view.set_tables import htmls
    # django 中重定向的 url 设定
    urls = [] 
    views = []
    # 从 static 往后, 除去 html 作为它的模板
    for html in htmls:
        filename_split = str(html).split("\\")
        temp_url = ""
        filename_split[len(filename_split)-1] = filename_split[len(filename_split)-1].replace(".html", "") 
        for x in range(len(filename_split)):
            if filename_split[x] == "static":
                static_index = x
                break
        urls.append("/".join(filename_split[x+1:]))
        views.append("_".join(filename_split[x+1:]))
            
    html_df = pd.DataFrame(np.array([htmls, urls, views]).T, columns=["html", "url", "view"])
    # print(html_df)
    html_df.to_csv("../data/html.csv")
    return html_df

# url_config()
## 复制更新模板环节 <== 替换所有文件逐行查找模板; 发现比较 （最后解决）
def extract_static_all_html(html):
    # 对每个 html 模板中有关路径的对象全部进行替换 
    pass 


"""
def `view`(request):
    return HttpResponse("appo\"+`view`.html)
"""
def write_url_view():
    df = url_config()
    with open("../py_data/views2.py", "w+", encoding = "UTF-8") as f:
        f.write("from django.shortcuts import render \n\n\n")
        for i in range(len(df)):
            string = '''def %s(request):\n    return render(request, "%s/%s.html")\n\n\n'''%(df.at[i, "view"], APP_NAME ,df.at[i, "view"])
            f.write(string)
        f.close()
    
    with open("../py_data/urls.py", "w+", encoding = "UTF-8") as f:
        f.write("from django.conf.urls import url \napp_name = '"+ APP_NAME +"'\nfrom . import views2 \n\n\n")
        f.write("urlpatterns = [\n")
        for i in range(len(df)):
            string = "    url(r'^%s/$', views2.%s, name='%s'),\n" % (df.at[i, "url"], df.at[i, "view"], df.at[i, "view"])
            f.write(string)
        
        f.write("\n]\n")
        f.close()

## 写入两个TXT 本质上是 .py
write_url_view()

# from table_view.temp import DF
# print(DF)
### 终极难点 URL 替换环节 
def copy_html_to_template(html_df):
    
    for i in range(len(html_df)):    
        with open(html_df.at[i, "html"], "r+", encoding="UTF-8") as f:    
            with open("../appo/" + html_df.at[i, 'view'] + ".html", "w+", encoding = "UTF-8") as f2:
                f2.write(f.read())
                f2.close()
            f.close()

html_df = url_config()
# copy_html_to_template(url_config())
# 复制完毕后 根据 DF 中的原则进行替换。

# html 为公共的主键, 找到 html 的内容, 将每个html中对应的这个内容进行替换即可。理论上能够进行
### html 中 对应的html 一律对应为对应的 html_df 的 url; 同理 css 一律也是只选择 /static 后面的内容 

### 这里文件并不是很大所以我们遍历了两次所有的 html 文件; 现在计算非常快，所以略。还是可以重构的。

'''
    for i in range(len(html_df)):
        from tools.rule import Rules    
        with open(html_df.at[i, "html"], "r+", encoding="UTF-8") as f:    
            with open("appo/" + html_df.at[i, "view"] + ".html", "w+", encoding = "UTF-8") as f2:
                strings = f.readlines()
                ## 目前只针对前三个规则进行替换
                funcs = Rules().main()
                for hang in range(len(strings)):
                    for rule_id in range(len(funcs)):
                        if funcs[rule_id](strings[hang]):
                            if rule_id < 4:
                                pass 


                        else:
                            f2.write()

'''
                                
                    


