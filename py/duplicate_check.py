 # f = open('feedInfo.log')
    # lines = f.readlines()
    # for feed_id in lines
    #     print(i[feed_id])
# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: gentle.yu
# @Date:   2019-09-09 18:03:47

with open(r'/Users/yuyanchao/yyc/Work/golemon/bin/feedInfo_T.log','r') as f:
    log_str = f.read()
log_data = log_str.split('\n')
feed_num = 0
feed_data = {}
for i in log_data:
    if 'feed_id' in i:
        feed_num += 1
        if i.split('feed_id: ')[1].split(' ')[0] not in feed_data:
            feed_data[i.split('feed_id: ')[1].split(' ')[0]] = 0
        feed_data[i.split('feed_id: ')[1].split(' ')[0]] += 1
print(feed_num)
print(len(feed_data))
