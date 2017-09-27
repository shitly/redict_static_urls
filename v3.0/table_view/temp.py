import pandas as pd 
import numpy as np
import re

import os
from os.path import join, dirname, abspath
DIR = dirname(dirname(abspath(__file__)))

import sys
sys.path.insert(0, DIR)
"""
    处理规则文件夹
"""

from table_view.set_tables import df
# df = pd.DataFrame(arrays, columns = ["html", "hang", "rule_id", "string"])

def main():
    from table_view.set_tables import df
    olds = []
    news = []
    i = 0
    n = len(df)
    while i < n:

        if df.at[i, "rule_id"] == str(1):
            _old1 = re.findall('''.*?href="(.*?)".*?''', df.at[i, "string"])
            _old2 = re.findall('''.*?src="(.*?)".*?''', df.at[i, "string"])
            _old = [_old1 if _old1 else _old2][0]
            i_count = 0
            for old in [x for x in _old]:
                i_count += 1 
                filename_split = str(df.at[i, "html"]).split("\\")
                if i_count > 1:
                    # 插入一个复制的条目
                    df = pd.concat([df[0:i], df[i:i+1], df[i:]], ignore_index=True)
                    i += 1
                    n += 1

                # 统计点点的数量
                count_dd = 0  
                for c in old.split("/"):
                    if c == '..':
                        count_dd += 1
                
                ## html 对应的初始目录
                head_file = "\\".join(filename_split[0:(len(filename_split) -1 - count_dd)])
                new = ["" if old == "" else str(head_file) + "\\" + "\\".join(old.split("/")[count_dd:])][0]

                olds.append(old)
                news.append(new)
            
        if df.at[i, "rule_id"] == str(2):
            _old = re.findall('''.*url:\s*"(.*?)".*''', df.at[i, "string"])
            i_count = 0
            for old in [x for x in _old]:
                i_count += 1 
                filename_split = str(df.at[i, "html"]).split("\\")
                if i_count > 1:
                    ### 插入一个复制的条目
                    print("一行出现多条")
                    df = pd.concat([df[0:i], df[i:i+1], df[i:]], ignore_index=True)
                    i += 1
                    n += 1

                # 统计点点的数量
                count_dd = 0  
                for c in old.split("/"):
                    if c == '..':
                        count_dd += 1
                
                ## html 对应的初始目录
                head_file = "\\".join(filename_split[0:(len(filename_split) -1 - count_dd)])
                new = ["" if old == "" else str(head_file) + "\\" + "\\".join(old.split("/")[count_dd:])][0]

                olds.append(old)
                news.append(new)

        if df.at[i, "rule_id"] == str(3):
            _old = re.findall('''.*symbol:\s*'(.*?)'.*''', df.at[i, "string"])
            i_count = 0
            for old in [x for x in _old]:
                i_count += 1 
                filename_split = str(df.at[i, "html"]).split("\\")
                if i_count > 1:
                    # 插入一个复制的条目
                    print("一行出现多条")
                    df = pd.concat([df[0:i], df[i:i+1], df[i:]], ignore_index=True)
                    i += 1
                    n += 1

                # 统计点点的数量
                count_dd = 0  
                for c in old.split("/"):
                    if c == '..':
                        count_dd += 1
                
                ## html 对应的初始目录
                head_file = "\\".join(filename_split[0:(len(filename_split) -1 - count_dd)])
                new = ["" if old == "" else str(head_file) + "\\" + "\\".join(old.split("/")[count_dd:])][0]

                olds.append(old)
                news.append(new)
            
        if df.at[i, "rule_id"] == str(4):
            old = "diy_need"
            new = old
            olds.append(old)
            news.append(new)

        if df.at[i, "rule_id"] == str(5):
            _old = re.findall('''.*?url\('(.*?)'\).*''', df.at[i, "string"])
            i_count = 0
            for old in [x for x in _old]:
                i_count += 1 
                filename_split = str(df.at[i, "html"]).split("\\")
                if i_count > 1:
                    # 插入一个复制的条目
                    print("一行出现多条")
                    df = pd.concat([df[0:i], df[i:i+1], df[i:]], ignore_index=True)
                    i += 1
                    n += 1

                # 统计点点的数量
                count_dd = 0  
                for c in old.split("/"):
                    if c == '..':
                        count_dd += 1
                
                ## html 对应的初始目录
                head_file = "\\".join(filename_split[0:(len(filename_split) -1 - count_dd)])
                new = ["" if old == "" else str(head_file) + "\\" + "\\".join(old.split("/")[count_dd:])][0]

                olds.append(old)
                news.append(new)

        i += 1

    df["new"] = news
    df["old"] = olds
    df.to_csv("../data/temp.csv")
    return df

DF = main()
        

