# coding:utf-8 #设置编码格式

# 引入appium库中和webdriver包
from appium import webdriver
from time import sleep

# 定义一个desired_caps字典来保存启动APP所需的那5个参数
desired_caps = {'platformName': 'Android',
                'platformVersion': '9',
                'newCommandTimeout': '600',
                'deviceName': '2cd4b315ee1d7ece',
                'appPackage': 'com.golemon.wegoo.funny',
                'appActivity': 'com.GoLemon.MainActivity'}

# 通过webdriver包下面的Remote方法打开App
dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
sleep(10)

# 登录APP（掉起三方应用登录）
# dr.find_element_by_xpath("//android.widget.ImageView[@resource-id='com.golemon.wegoo:id/no']").click()
# dr.find_element_by_xpath("//android.widget.TextView[@resource-id='com.golemon.wegoo:id/bk']").click()
# #
# dr.find_element_by_xpath("//android.widget.TextView[@resource-id='com.golemon.wegoo:id/jh']").click()    # google登录
# dr.find_element_by_xpath("//android.widget.TextView[@resource-id='com.golemon.wegoo:id/hw']").click()    # facebook登录
