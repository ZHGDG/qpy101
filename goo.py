# -*- coding: utf-8 -*-
#qpy:webapp:goo.gl缩址墙内代理生成器
#qpy://localhost:8080/goo
from bottle import route, run, template
#import httplib, urllib
import sys
import os.path
app_root = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(app_root, "3party/"))
#from 3party 
import requests
#print dir(requests)

@route('/goo')
def index():
    return curl_goo()

def curl_goo():
    payload = {'uri': 'http://www.zhgdg.org'}
    r = requests.post("http://api.zhgdg.org/v0/goo", data=payload)
    print r.text
    return r.text

run(host='localhost', port=8080)
