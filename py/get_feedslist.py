#!/bin/python

# coding: utf-8  

import json
#import emoji

def get_json(text):
    return json.loads(text)

if __name__ == '__main__':
    f = open('feedlist.txt')
    text = f.readline()
    text = get_json(text)
    for i in text['data']['feeds']:
        print('feed_id:',i['feed_id'],'\tclass_id:',i['classId'],'\ttopic_id:',i['topic_id'],'\tcontent_type',i['content_type'])
        #print('tcontent_type',i['content_type'])
