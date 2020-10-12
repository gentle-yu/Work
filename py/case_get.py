# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: gentle.yu
# @Date:   2019-10-01 15:26:22

import requests

url = "http://funny.bc.test.golemon123.com/feeds/getFeedListRecommend?"

#请求头
headers = {
	
	"Connection": "Keep-Alive",
	"Host": "funny.bc.test.golemon123.com",
	"lang": "es-MX",
	"User-Agent": "Mozilla/5.0 (Linux; Android 7.1.2; SM-G955F Build/JLS36C; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/75.0.3770.143 Mobile Safari/537.36; GoLemon_1.2.0",
	"QnmAuth": "eyJpdiI6ImJOQ3ZDU2p0MlhPU1pBdGtLeWY5WkE9PSIsInZhbHVlIjoiZ3JvaHN0WDNWMEk4dWpEUnc4a2xHZTZsZnVnQ1NmeVBOOFJiaHkwbVdlczUwR3ByN2xQUFB4cU9QS2FJYiszOCtzM09sVmErSXc4MXp3bWRZVWVpMGYwSFpLcWcxY3JNRVZxanB0amlKckxoZjkyTVhhR0pGbEwzQlg5QkU4b21xOFVOTzJGUEhKN3pzQTZZbGlDbDFWWnJCZGVhblRBdld0cGl0c09JN01LS3o3QW9Yb3hvSUthRENWTkV6WFFtUDJyc3NZU3NsSkdKVjllaTZwaXRmaFVUa21PR1lQdHBQd2tmVGJpNzJ5RW91NlJFYkFzUlZqQjg5c1lzeDJQQW84bWUydk1rUVBoa0dncEV3TjJ6WnBkNjhXS1EzYWZ0SklSUDVWTVRDMnV0d1dONFpZS1ExcjZDbm03QjlheHR1c3FhUTdoU2QyMnFDZytsMjFvWCtvMVpob0lSZGJFMzFadDg3TG00RmJRMDBxSzlGb29oU1dOZ2ZGTHdjT1c0SUZWNUxRNXNpZVlLamphSzJKa1VEMEg3WUE0RFYxbHJrQWJPV0dTcUNhd0VxYk05MGljTlVoY1k4eGFzeXo2SWtkZDZxM093aHdlVXVVVVZwWU9GQ0E9PSIsIm1hYyI6IjQ4MzAyNzY3ZmM4OGM5NTFkZDIzOWJlNTIxYmJmYWJmOWQ1NTdhN2EyYzcxMDAyMDU0M2YxMTQ3ODM2NTJkMDMifQ==",

}

###http://funny.bc.test.golemon123.com/feeds/getFeedListRecommend?time_begin=1569914878294&v=1.2.0&network=wifi&is_refresh=1&md=SM-G955F&m2=840984ac5b3afbff58e39280c0ac0a3d&sign=420a687d1f5f3cb7f486242c9f58aa04&tm=1569914891602&offset=0&mf=samsung&num=10&channel=funny&os=Android

#URL参数

payload = {"time_begin":"1569914878294","v":"1.2.0","network":"wifi","is_refresh":"1","md":"SM-G955F","m2":"840984ac5b3afbff58e39280c0ac0a3d","sign":"420a687d1f5f3cb7f486242c9f58aa04","tm":"1569914891602","offset":"0","mf":"samsung","num":"10","channel":"funny","os":"Andoroid"}

#设置访问代理

# proxies = {
	
# 	"https": "http://39.106.224.202",
# 	"https": "http://125.123.127.213",
# }

#发送get请求

# reponse = requests.get(url,headers=headers,params=payload,proxies=proxies)

reponse = requests.get(url,headers=headers,params=payload)

"""
print u'HTTP状态码:',r.status_code
print u'请求的URL:',r.url
print u'获取Headers:',r.headers
print u'响应内容:',r.text
"""

#查看相应内容

print(reponse.text)

#查看响应代码

print(reponse.status_code)

#查看请求的url

print(reponse.url)

#查看获取的headers

print(reponse.headers)

