import pandas as pd 
import numpy as np
import re

import os
from os.path import join, dirname, abspath
DIR = dirname(dirname(abspath(__file__)))

import sys
sys.path.insert(0, DIR)
## 解决本地静态文件测试的重写

from table_view.temp import DF
from table_view.pcl import html_df


def split_url(url):
    filename_split = str(url).split("\\")
    temp_url = ""
    for x in range(len(filename_split)):
        if filename_split[x] == "static":
            break
    if re.match(".*?(.html).*?", filename_split[len(filename_split)-1]):
        return "_".join(filename_split[x+1:])

    return "/".join(filename_split[x+1:])



new_htmls = [x+".html" for x in html_df["view"]]
html_df["new_html"] = new_htmls

dff = pd.merge(DF, html_df, on="html", how="inner")
pre_puts = [split_url(x) for x in dff["new"]]

# dff.to_csv("summary.csv")
for i in range(len(html_df)):
    gaim_df = dff[dff["html"]==html_df.at[i, "html"]]
    with open(html_df.at[i, "html"], "r+", encoding="UTF-8") as f1:
        strings = f1.readlines()
        with open("../appo/"+ html_df.at[i, "new_html"], "w+", encoding="UTF-8") as f2:
            j = 0
            while j < len(strings):
                if j in gaim_df["hang"]:
                    # 该行需要改动; 那么遍历这个行; 替换我们需要修改的目标内容
                    modify_df = gaim_df[gaim_df["hang"] == j]
                    # 如果该行有多处; 那么就一次修改多处
                    for k in range(len(modify_df)):
                        rule_id = modify_df.at[k, "rule_id"]
                        # index = modify_df.at[k, "hang"]
                            
                        if int(rule_id) != 4:
                            pre_put = strings[j].replace(modify_df.at[k, "old"], split_url(modify_df.at[k, "new"]))
                            f2.write(pre_put)
                        else:
                            f2.write(strings[j])
                            # f2.writeline() 第四种情况修改后的结果
                else:
                    f2.write(strings[j])

                j += 1
            f2.close()
        f1.close()
                

            