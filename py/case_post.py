# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: gentle.yu
# @Date:   2019-10-01 16:05:28

import requests

url="http://127.0.0.1:8090/recruit.students/login/in?"

#把请求头信息进行处理，去掉一些没用的，保留一些有用头信息·

headers = {

    "Connection": "keep-alive",

    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",

    "Referer": "http://127.0.0.1:8090/recruit.students/login/view",

  }

# URL参数

payload = {'account': 'admin','pwd':'660B8D2D5359FF6F94F8D3345698F88C'}

# 发送Post请求

response = requests.post(url,headers = headers,data=payload)



# 查看响应内容，response.text 返回的是Unicode格式的数据

print(response.text)

# 查看响应码

print(response.status_code)