#!/usr/bin/python
# Another api to operate the weibo, not so powerful but seems
# enough for me.
# my request is just post/delete/list/set the visibility,
# that's all. 

api_key='1804308942'
status='hello'
userid='batman.wang@qq.com'
password='168802'
post_url='https://api.weibo.com/2/statuses/update.json'
delete_url='https://api.weibo.com/2/statuses/destroy.json'
read_url=''
visible=1

curl -u batman.wang@qq.com:168802 -d "source=&status="hello"&visible=1" https://api.weibo.com/2/statuses/update.json
