# README.txt

## 这是一个开发文档，关于本 APP 静态文件的 HTML 全部加载到 模板里面 进行隐藏的过程。

### 静态文件初步观察和理解。

#### 目录结构的使用和调整。

==> 凡是 href | src全部修改为 static 的根目录 /static/__file__/__file__/
    => ../ 文件的处理; 归结到父目录名字, 替换 .. 为父目录

==>  url: "svg/topo_1000_590.svg",
==> required 包的设置; 
            paths: {
                'echarts': '../../js/echartmap/echarts',
                'echarts/chart/map': '../../js/echartmap/map'
            }
==> symbol:'image://img/attacker.png',

++
==> :url('../../img/new8_1.png');"
==> img 的 

## 处理环节

### 开发前的考虑

1, 记录所有要修改的 html 位置; /static/...
2, 记录在该 html 中所有涵盖目标标签的 url 写法, url 位置; url修改后的情况, 该字段所在html行。
3, 再进行 new_html 替换实验, 首先目标不要修改为 /static/ 而是 static/ 这样是便于在 static 目录下测试


#### 开发设计思路
==> 数据库需要记录的字段; 该html的ID 表1, html总览
    rule_html 
    字段 => 记录所有情况的 ID, 情况描述, 情况示例, 情况

    table_html 
    字段 => html 位置 涵盖父目录。

    html_element table
    字段 => url 整行所属情况ID, url 所在行; url位置; url 修改后的位置。

#### 开发进行中

=========== 规则挖掘 rule.py ==============
    0, rule_table 的初始化。 <== 通过观察得到的所有规则

=========== 规则展示 set_tables.py ==============
    1, 扫描整个目录, 将所有的html 记录下来; html 深度。
    2, 对每个html内部凡是不以 \ 开头的全部 `正则` 记录下来; 分布所在情况, 将字段写入 html_element 表格
    3, new_html 测试调整: 对每个 html 进行按需调整, 全部归结到 static/ 下

=========== html 重定向模块 pcl.py ==============
    1, 对每个 html 进行定向下一步; 重定向, 链接选择—脚本; redirect_url.py
    2, views.py 里面进行渲染的 批量脚本 pcl.py  view -> url -> html模板


    
