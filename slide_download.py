#!/usr/bin/python
# Some slides on the slideshare.net is not allowed to download, the easy way
# to 'save' is save the slides as picture when view them; 
# This script is used to download the picture.

#TODO: 
# 1. Is it possible to insert the pictures to the powerpoint automatically?
# 2. exception handling, if the download is fail? the timeout? file saving fail?
# 3. if need to use proxy?

import urllib
import urllib2
import os
import time
import re
import pdb
from sys import argv

if len(argv) != 3:
    print "usage:"
    print "python %s <url> <pages>" % __file__
    print "\nHow to get the 'url' --"
    print "\tMaximize the slide page, right click the picture page, get the picture's link, that's the 'url'"
    exit()
else:
    script, url, pages = argv
    print "%s" % url
    print "%s" % pages

#url="http://image.slidesharecdn.com/dragonflowl3sdnmeetup-150720064301-lva1-app6891/95/openstack-neutron-dragonflow-l3-sdnmeetup-1-1024.jpg?cb=1437376671"

for a in range(1,int(pages)+1):
    print a
    if a > 10:
        #any way to not aware the width of the number?
        url = re.sub(r"-..-1024", "-%s-1024" %a, url)
#        pdb.set_trace()
    else:
        url = re.sub(r"-.-1024", "-%s-1024" %a, url)

    pic_url = url.split('?')[:-1]
    file_name = url.split('/')[-1].split('?')[0]
#    print "%s" %url
#    print "%s" %pic_url[0]
#    print "%s" %file_name
    urllib.urlretrieve(pic_url[0], file_name)
#    time.sleep(1) #download picture take times, no need to wait

print "done!"    
exit()

