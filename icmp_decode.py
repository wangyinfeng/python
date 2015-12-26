#!/usr/bin/env python
import pdb
import ast
import re
import os
import time
import subprocess

# Make sure ping is OK before do the delay test

#TODO 
# lunch the ping and tcpdump, save the output to file and do strip
# decode the output, save the timestamp, requrest/reply, id, seqnum

# find the proper messages group - 4 request + 4 request, same id and same seqnum and different timestamp
# find 5 groups
# find the request/reply pairs and count the time difference
# count the average time spent on the path
# print the result

# capture all packet by commands
# tcpdump -i eth1 vlan and icmp & tcpdump -i any icmp

PAIRS = 4
MIN_PACKETS = PAIRS*2
SEQS = 5

class Icmp(object):
    def __init__(self):
        self.ts = 0
        self.id = 0
        self.seq = 0
    def __repr__(self):
        return '{}: {} {}'.format(self.__class__.__name__,
                                  self.ts)

def get_key(icmp):
    return icmp.ts

with open('dump') as f:
    content = f.readlines()
request = []
reply = []

for line in content:
    # id should be given, and filter the packets by the id first
    if 'id 3644' not in line:
        continue
    print line
    e = line.split()
    #pdb.set_trace()
    # only handle icmp echo 8/0
    if ('request' not in e[7]) and ('reply' not in e[7]):
        continue

    pkt = Icmp()
    pkt.ts = float(e[0])
    pkt.id = int(e[9][:-1])
    pkt.seq = int(e[11][:-1])
    if 'request' in e[7]:
        request.append(pkt)
    else:
        reply.append(pkt)

# sort the object
#pdb.set_trace()
request = sorted(request, key=get_key)
reply = sorted(reply, key=get_key)
seqs = []
for i in request:
    print "%f" %i.ts
    seqs.append(i.seq)

# get the sequence number list
seqs = list(set(seqs))  # remove duplicated
for i in seqs:
    print i

# get the valid request-reply pair
# filter by sequence, if the packets with the sequence less than PAIRS*2, 
# remove out, if the left less than PAIRS*2, drop the task
#new_request = request
#new_reply = reply
for s in seqs:
    n = 0
    for i in request:
        if s == i.seq:
            n=n+1
    if n != PAIRS:
        #pdb.set_trace()
        print "sequence number %d removed" %s
        seqs.remove(s)
        request[:] = (v for v in request if v.seq != s)
        reply[:] = (v for v in reply if v.seq != s)
        #filter(lambda a: a.seq != s, request)
        #filter(lambda a: a.seq != s, reply)

    if len(request) < PAIRS or len(reply) < PAIRS:
        print "No enough validate packets, drop the task"
        break


# count the time

# echo the result
    

def get_data():
    eth_process = subprocess.Popen(['tcpdump', '-i', 'eth1', 'vlan and icmp', '-nn', '-tt', '-c 1000'],
                                  stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    any_process = subprocess.Popen(['tcpdump', '-i', 'any', 'icmp', '-nn', '-tt', '-c 1000'],
                                  stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    time.sleep(5)
    eth_process.terminate()
    any_process.terminate()
    eth_process.wait()
    any_process.wait()
    result_eth = eth_process.stdout.read() 
    result_any = any_process.stdout.read() 
    # TODO need to do filter to get necessary data
    print result_eth+result_any
    print "======================================================="

#get_data()

def main():
    print "hello"

if __name__ == "__main__":
    main()

