#coding: utf-8
# The practice about spider. Get all diaries and photos about Renxiaowen@douban.
# Save the diaries to a directory, named by the date when create the diary;
# and save the photos to another directory, named by any name you like.
import sys
import os
import re   #support for regular expressions
import time
import urllib
import urllib2
import requests #HTTP library
from bs4 import BeautifulSoup #parse a document to a tree representation

import pdb


file_name = ''
file_content = ''
file_content = ''

base_url = "http://www.douban.com/people/renxiaowen/"
item_note = "notes"
item_photo = "photos"

def get_notes():
    global file_content

    url = base_url + item_note
    source_code = requests.get(url)
    # just get the code, no headers or anything
    plain_text = source_code.text
    # BeautifulSoup objects can be sorted through easy
    soup = BeautifulSoup(plain_text)

    title_divide = '\n' + '--' * 30 + '\n' + '--' * 30 + '\n'
    count = 1
    
    list_soup = soup.findAll('div', {'class': 'note-header-container'})
#    pdb.set_trace()
    for notes in list_soup:
        note_link = notes.find('a', {'class':'j a_unfolder_n'}).get('href')
        print note_link
        count += 1


def do_spider():
    get_notes()

do_spider()

# 将最终结果写入文件
#f = open(file_name, 'w')
#f.write(file_content)
#f.close()
#print file_content
