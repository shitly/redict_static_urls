import pandas as pd 
import re
import numpy as np


class Rules():
    
    def rule_0(self, string):
        return False 

    # 第一种情况: 凡是 href 全部修改为 static 的根目录 /static/__file__/__file__/ 还有 ../
    ## 返回的是所要求的 old, new, abs 的字段
    def rule_1(self, string):
        if re.match('''.*href="(.*?)".*''', string) or re.match('''.*src="(.*?)".*''', string):
            return True
        return False 

    # 第二种情况: url: "svg/topo_1000_590.svg",
    def rule_2(self, string):
        if re.match('''.*url: "(.*?)".*''', string) or re.match('''.*url:"(.*?)".*''', string):
            return True
        return False 

    # 第三种情况: symbol:'image://img/attacker.png',
    def rule_3(self, string):
        if re.match('''.*symbol:/s*'(.*?)'.*''', string):
            gaim = re.findall('''.*symbol:/s*'(.*?)'.*''', string)
            if gaim == "circle":
                return False
            return True
        return False 
    
    # 第四种情况: echart 的 require 情况
    def rule_4(self, string):
        if re.match('''.*paths: {.*''', string):
            return True
        return False 

    # 第五种情况, 背景图 url('../../img/new8_1.png') 右斜线为转义符号
    def rule_5(self, string):
        if re.match('''.*?url\('(.*?)'\).*''', string):
            return True
        return False 

    # 第六种情况, re.match('''.*src="(.*?)".*''', string)  单引号
    def rule_6(self, string):
        if re.match('''.*src='(.*?)'.*''', string):
            return True
        return False 

    def main(self):
        return [self.rule_0, self.rule_1, self.rule_2, self.rule_3, self.rule_4, self.rule_5]
        # return [self.rule_0, self.rule_1, self.rule_2, self.rule_3, self.rule_4, self.rule_5, self.rule_6]
        
        
    
    
    
    
    
