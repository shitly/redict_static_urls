import pandas as pd 
import re
import numpy as np


class Rules():
    
    def rule_0(self, string):
        return False 

    # 第一种情况: 凡是 href 全部修改为 static 的根目录 /static/__file__/__file__/ 还有 ../
    ## 返回的是所要求的 old, new, abs 的字段
    def rule_1(self, string):
        if re.match('''.*href="(.*?)".*''', string):
            return True
        return False 

    # 第二种情况: url: "svg/topo_1000_590.svg",
    def rule_2(self, string):
        if re.match('''.*url: "(.*?)".*''', string) or re.match('''.*url:"(.*?)".*''', string):
            return True
        return False 

    # 第三种情况: symbol:'image://img/attacker.png',
    def rule_3(self, string):
        if re.match('''.*symbol:'(.*?)'.*''', string) or re.match('''.*symbol: '(.*?)'.*''', string):
            return True
        return False 
    
    # 第四种情况: echart 的 require 情况
    def rule_4(self, string):
        if re.match('''.*paths: {.*''', string):
            return True
        return False 


    def main(self):
        return [self.rule_0, self.rule_1, self.rule_2, self.rule_3, self.rule_4]
        
        
    
    
    
    
    
