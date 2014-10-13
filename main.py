# -*- coding: utf-8 -*-
#qpy:webapp:goo.gl缩址墙内代理生成器
#qpy://localhost:8080/
from bottle import debug, run
from bottle import route
from bottle import error
from bottle import redirect, abort
from bottle import request, response
from bottle import static_file
from bottle import template
from bottle import TEMPLATE_PATH
#import httplib, urllib
import sys
import os.path
_app_root = os.path.dirname(__file__)
CUSTOM_TPL_PATH = os.path.abspath(
    os.path.join(
        _app_root
        , "views/")
    )
TEMPLATE_PATH.insert(0, CUSTOM_TPL_PATH)
sys.path.insert(0, os.path.join(_app_root, "3party/"))
import requests
#print dir(requests)


@route('/')
def index():
    return template('main')

@route('/goo', method='POST')
def goo():
    uri = request.forms.get('uri')
    return template('goo'
           , result = curl_goo(uri)
           )

def curl_goo(uri):
    payload = {'uri': uri}
    r = requests.post("http://api.zhgdg.org/v0/goo", data=payload)
    #print "r.keys\n\t", r.keys()
    uris = r.text.split('\n')
    return uris


@error(404)
def error404(error):
    return template('404')

@route('/favicon.ico')
def favicon():
    abort(204)
    
@route('/static/<filepath:path>')
def server_static(filepath):
    #print _app_root+'/static'
    return static_file(filepath, root = _app_root+'/static')

run(host='localhost', port=8080)
