#!/bin/python
# -*- coding: utf-8 -*-
# Post weibo from command line, such as:
# ~python weibo_post.py "the world you want to say"
# step1 - post text 
# step2 - post text and set the visibility, privite or public or share with friends
# step3 - support list and delete instance
# step4 - ...
#
# reference http://www.cnblogs.com/GentlemanMod/p/3263531.html

from weibo import APIClient
import urllib
import httplib
import requests 

import pdb

debug = 1

user_agent = (
  'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.11 (KHTML, like Gecko) '
  'Chrome/20.0.1132.57 Safari/536.11'
)
session = requests.session()
session.headers['User-Agent'] = user_agent
session.headers['Host'] = 'api.weibo.com'

global api_key, api_secret, callback_url, userid, password
api_key = '1804308942'
api_secret = '9d5650fb779595187f73df3ffbe2bdac'
#callback_url = 'http://127.0.0.1:3000/users/auth/weibo/callback'
#callback_url = 'http://sinaweibopy.sinaapp.com/'
#callback_url = 'https://api.weibo.com/oauth2/default.html'
callback_url = 'www.me.me'
#callback_url = 'https://api.weibo.com/oauth2/authorize?redirect_uri=http%3A//sinaweibopy.sinaapp.com/callback&response_type=code&client_id=2373761036'
userid = 'batman.wang@qq.com'
password = 'xxxxxx'

global client, referer_url
client =  APIClient(app_key=api_key, app_secret=api_secret, redirect_uri=callback_url)
referer_url = client.get_authorize_url()
if debug: print 'referer_url: %s' % referer_url

def get_code():

  data = {
    'client_id': api_key,
    'redirect_uri': callback_url,
    'userId': userid,
    'passwd': password,
    'isLoginSina': '0',
    'action': 'submit',
    'response_type': 'code'
  }

  session.headers['Referer'] = referer_url

  resp = session.post(
    url = 'https://api.weibo.com/oauth2/authorize',
    data = data
  )
  
  if debug: print 'get url: %s' % resp.url
  if debug: print 'code is: %s' % resp.url[-32:]
  
  code = resp.url[-32:]
  return code


def weibo_text(text):
  code = get_code()

  token = client.request_access_token(code)
  client.set_access_token(token.access_token, token.expires_in)

  client.statuses.update.post(status=text)

if __name__ == '__main__':
  weibo_text('testing')

