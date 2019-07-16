#!/usr/bin/python
# -*- coding: utf-8 -*-  
"""
@version : 
@file : api_client.py
@time : 2019/07/10 23:17:49
@func : 
"""
#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests


url="http://127.0.0.1:5000/"  # local test
# url="http://47.107.177.19:8088/"  # remote test

responses=requests.get(url)
print(responses)
# 查看响应内容，response.text 返回的是Unicode格式的数据
print(responses.text)
print(responses.content)
