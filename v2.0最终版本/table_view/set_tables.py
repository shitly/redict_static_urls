import pandas as pd 
import numpy as np
import re

import os
from os.path import join, dirname, abspath
DIR = dirname(dirname(abspath(__file__)))

import sys
sys.path.insert(0, DIR)

## MAIN
from tools.rule import Rules

from config import *

gaim_dir = STATIC_ROOT
files = os.listdir(gaim_dir)

def find_html(path, allfile):  
    filelist =  os.listdir(path)  
    for filename in filelist:  
        filepath = os.path.join(path, filename)  
        if os.path.isdir(filepath):  
            find_html(filepath, allfile)
        else:
            if re.match(".*.html.*", repr(filepath)): 
                allfile.append(filepath)
                # 这个环节可以复制 html 到对应目录下   
    return allfile  

allfile = []
htmls = find_html(gaim_dir, allfile)
# [print(x) for x in htmls]

array = []

def find_element(html):
    array = []
    with open(html, "r+", encoding='UTF-8') as f:
        strings = f.readlines()
        funcs = Rules().main()
        for hang in range(len(strings)):
            for rule_id in range(len(funcs)):
                if funcs[rule_id](strings[hang]):
                    # print("在 "+ str(html) + " 的第 "+ str(hang) +" 行匹配到规则 "+ str(rule_id))
                    array.append([str(html), str(hang), str(rule_id), strings[hang]])
                    break
        f.close()
    return array

arrays = []    
for html in htmls:
    arrays.extend(find_element(html))

df = pd.DataFrame(arrays, columns = ["html", "hang", "rule_id", "string"])


