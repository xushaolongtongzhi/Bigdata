
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : lenshao Xu (1154973714@qq.com)
# @Version : 0.0.1
import requests
import json
import time, threading
import sys
def send_mail(toMail,sub,content,cc=None):
    headers = {'Content-Type':'application/json'}
    data = {"to":toMail,
            "cc":'',
            "accessToken":'9975681ab2e64ebd9e878fc01c0318268db8caaeb3f943a99b36e780cac261b7',
             "html":'false',
            "subject":sub,
            "system":"False",
            "content":content
    }


    values = json.dumps(data)
    #headers = json.dumps(headers)
    # url ='http://10.129.4.95:90/data_manage/'
    url='http://196.168.100.77/mail-dmz-internet/email/v1/'
    r = requests.post(url,values,headers=headers)
    print r
    print(r.text)
if __name__ == '__main__':
    toMail=sys.argv[1]
    sub=sys.argv[2]
    content=sys.argv[3]
    print "toMail: %s"%sys.argv[1]
    print "sub: %s"%sys.argv[2]
    print "content: %s"%sys.argv[3]
    send_mail(toMail,sub,content)
