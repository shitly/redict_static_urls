import pandas as pd 
import numpy as np
import re

import os
from os.path import join, dirname, abspath
DIR = dirname(dirname(abspath(__file__)))

import sys
sys.path.insert(0, DIR)
## 解决本地静态文件测试的重写

from config import ECHARTS, ECHARTS_MAP, APP_NAME
from table_view.temp import DF
from table_view.pcl import html_df


def split_url(url):
    filename_split = str(url).split("\\")
    temp_url = ""
    for x in range(len(filename_split)):
        if filename_split[x] == "static":
            break
    ## html 匹配到静态模板; 但是在Django中就应该匹配到对应的链接 /appo/ + url
    if re.match(".*?(.html).*?", filename_split[len(filename_split)-1]):
        #return "_".join(filename_split[x+1:])
        filename_split[len(filename_split)-1] = filename_split[len(filename_split)-1].replace(".html", "") 
        return "/" + APP_NAME + "/" + "/".join(filename_split[x+1:])
        
    return "/static/" + "/".join(filename_split[x+1:])


new_htmls = [x+".html" for x in html_df["view"]]
html_df["new_html"] = new_htmls

dff = pd.merge(DF, html_df, on="html", how="inner")
pre_puts = [split_url(x) for x in dff["new"]]

# dff.to_csv("summary.csv")
for i in range(len(html_df)):
    gaim_df = dff[dff["html"] == html_df.at[i, "html"]]
    with open(html_df.at[i, "html"], "r+", encoding="UTF-8") as f1:
        strings = f1.readlines()
        with open("../"+ APP_NAME +"/"+ html_df.at[i, "new_html"], "w+", encoding="UTF-8") as f2:
            j = 0
            while j < len(strings):
                if str(j) in list(gaim_df["hang"]):
                    # 该行需要改动; 那么遍历这个行; 替换我们需要修改的目标内容
                    modify_df = gaim_df[gaim_df["hang"] == str(j)]
                    # 如果该行有多处; 那么就一次修改多处

                    _olds = list(modify_df["old"])
                    _news = list(modify_df["new"])
                    rule_ids = list(modify_df["rule_id"])
                    for k in range(len(modify_df)):
                        rule_id = rule_ids[k]
                        # index = modify_df.at[k, "hang"]
                        if int(rule_id) != 4:
                            pre_put = strings[j].replace(_olds[k], split_url(_news[k]))
                            f2.write(pre_put)
                        else:
                            f2.write(strings[j])
                            # f2.writeline() 第四种情况修改后的结果
                            first = strings[j+1]
                            second = strings[j+2]
                            old_first =re.findall('''.*?'echarts':\s*'(.*?)'.*?''', first)
                            old_second =re.findall('''.*?'echarts/chart/map':\s*'(.*?)'.*?''', second)
                            new1 = strings[j+1].replace([i for i in old_first][0], ECHARTS)
                            new2 = strings[j+2].replace([i for i in old_second][0], ECHARTS_MAP)
                            f2.write(new1)
                            f2.write(new2)
                            j += 2
                else:
                    f2.write(strings[j])

                j += 1
            f2.close()
        f1.close()
        # 产品环境下这里可以删除掉 static 中的html 了
                

            