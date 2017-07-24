import pandas as pd 
import numpy as np
import re

import os
from os.path import join, dirname, abspath
DIR = dirname(dirname(abspath(__file__)))

import sys
sys.path.insert(0, DIR)
# 处理规则文件夹

from table_view.set_tables import df
# df = pd.DataFrame(arrays, columns = ["html", "hang", "rule_id", "string"])


def main():
    
    olds = []
    news = []

    for i in range(len(df)):

        if df.at[i, "rule_id"] == str(1):
            old = re.findall('''.*href="(.*?)".*''', df.at[i, "string"])[0]
            filename_split = str(df.at[i, "html"]).split("\\")
            # 统计点点的数量
            count_dd = 0  
            for c in old.split("/"):
                if c == '..':
                    count_dd += 1
            
            ## html 对应的初始目录
            head_file = "\\".join(filename_split[0:(len(filename_split) -1 - count_dd)])
            
            if old = "":
                new = ""
                
            olds.append(old)
            news.append(str(head_file) + "\\" + "\\".join(old.split("/")[count_dd:]))

        if df.at[i, "rule_id"] == str(2):
            old = re.findall('''.*url:\s*"(.*?)".*''', df.at[i, "string"])[0]
            new = old
            olds.append(old)
            news.append(new)

        if df.at[i, "rule_id"] == str(3):
            old = re.findall('''.*symbol:\s*'(.*?)'.*''', df.at[i, "string"])[0]
            new = old
            olds.append(old)
            news.append(new)
            
        if df.at[i, "rule_id"] == str(4):
            old = "diy_need"
            new = old
            olds.append(old)
            news.append(new)

    df["old"] = olds
    df["new"] = news
    df.to_csv("t.csv")
main()
        

