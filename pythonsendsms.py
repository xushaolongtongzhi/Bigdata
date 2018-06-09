#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : lenshao Xu (1154973714@qq.com)
# @Version : 0.0.1
import requests
import json
import time, threading
import sys
def send_mail(phone,content,cc=None):
    headers = {'Content-Type':'application/json'}
    data = {"phone":str(phone),
            "content":content
    }
 
    #data = {"phone":"17512059329","content":"xushaolongtongzhi"}
 
    values = json.dumps(data)
    #headers = json.dumps(headers)
    #url ='http://10.129.4.95:90/data_manage/'
    url="http://196.168.100.77/mail-dmz-internet/sms"
    #url='http://196.168.100.77/beacon-internet-email-node/sendSMS/v1/'
    #r = requests.post(url,values,headers=headers)
    r = requests.post(url,values,headers=headers)
    print(r.text)
if __name__ == '__main__':
    phone=sys.argv[1]
    content=sys.argv[2]
    #print "phone: %s"%sys.argv[1]
    #print type(phone)
    #print "content: %s"%sys.argv[2]
    send_mail(phone,content)
