#!/usr/bin/python
# Another api to operate the weibo, not so powerful but seems
# enough for me.
# my request is just post/delete/list/set the visibility,
# that's all. 
#
# The content is encrypted
#
# {"error":"parameter (visible)'s value invalid,expect (visible != 1), but get (1), see doc for more info.","error_code":10017,"request":"/2/statuses/update.json"}
# The fucking API not support post private (visible=1),
# useless for me. I only want to post private, take it as
# personal log.

from datetime import datetime
import requests

api_key='1804308942'
status=str(datetime.now())
userid='batman.wang@qq.com'
password='xxxxxx'
post_url='https://api.weibo.com/2/statuses/update.json'
delete_url='https://api.weibo.com/2/statuses/destroy.json'
read_url='https://api.weibo.com/2/statuses/user_timeline.json'
visible=2

#curl -u batman.wang@qq.com:xxxx -d "source=1804308942&status="hello"&visible=2" https://api.weibo.com/2/statuses/update.json

# -d send the specified data in the POST request to server
# -u specified the username and password


data = {
    'source':api_key,
    'status':status,
    'visible':2
        }

# not PUT
resp = requests.post(
        post_url,
        auth = (userid,password),
        data = data
        )

print resp.status_code
