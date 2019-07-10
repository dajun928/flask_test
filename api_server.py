#!/usr/bin/python
# -*- coding: utf-8 -*-  
"""
@func : 阿里云部署Flask项目
@file : api_server.py
@time : 2019/07/02 00:42:13
@url : https://www.jianshu.com/p/9293cc21a571?utm_campaign=maleskine&utm_content=note&utm_medium=seo_notes&utm_source=recommendation
"""

#导入Flask扩展
from flask import Flask,render_template

# 创建Flask应用实例
app = Flask(__name__)

# 定义路由及视图函数
@app.route('/')
def hello_world():
    return 'Hello world!'


# 启动程序
if __name__ == '__main__':
    app.run(debug=True)
