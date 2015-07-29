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

#Error: maximum recursion depth exceeded while calling a Python object
sys.setrecursionlimit(1000)
#where do I use the recursion?

file_name = ''
file_content = ''
note_links = []

base_url = "http://www.douban.com/people/"
people = "renxiaowen"
item_note = "notes"
item_photo = "photos"


def get_note_links():
    global file_content
    global note_links

    url = base_url + people + '/' + item_note
    source_code = requests.get(url)
    # just get the code, no headers or anything
    plain_text = source_code.text
    # BeautifulSoup objects can be sorted through easy
    soup = BeautifulSoup(plain_text)

    title_divide = '\n' + '--' * 30 + '\n' + '--' * 30 + '\n'
    count = 1
    pages_info = soup.find('div', {'class':'paginator'})
    pages_num = int(pages_info.find('span', {'class':'thispage'}).get('data-total-page'))
    page_url = []
#    page_url.append(url)
    for page in pages_info.find_all('a'):
        page_url.append(page.get('href'))
    #last one item is duplicated    
    page_url.pop()
    
    #get the 1st page note links
    list_soup = soup.findAll('div', {'class': 'note-header-container'})
    for notes in list_soup:
        note_link = notes.find('a', {'class':'j a_unfolder_n'}).get('href')
        note_links.append(note_link)
        count += 1
    
    #get the remain pages note links
    for next_page in page_url:
        url = next_page
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        list_soup = soup.findAll('div', {'class': 'note-header-container'})
        for notes in list_soup:
            note_link = notes.find('a', {'class':'j a_unfolder_n'}).get('href')
            note_links.append(note_link)
            count += 1

def get_note_content(link):
    source_code = requests.get(link)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    content = soup.find('div', {'id': 'link-report'})

    note_date = soup.find('span', {'class':'pl'}).string.partition(' ')[0]
    #os.path.join know whether to use '\' or '/'
    file_name = os.path.join(people, note_date)
    
    file_content = str(content).replace("<br>", "\n").replace("</br>", "\n") + "\n"
    f = open(file_name, 'w')
    f.write(file_content)
    f.close()
    print file_content


def do_spider():
    get_note_links()
    print note_links

    if not os.path.exists(people):
        os.makedirs(people)

    for link in note_links:
        get_note_content(link)

do_spider()

