#!/usr/bin/env python
import pdb
import dpkt
from dpkt.ip import IP_PROTO_ICMP
from dpkt.ethernet import ETH_TYPE_IP
from dpkt.icmp import ICMP_ECHOREPLY
from dpkt.icmp import ICMP_ECHO

SSL_HEADER = '\x00\x01\x00\x06'
ETHERNET_II = 0
LINUX_SSL = 1

class pkt_icmp(object):
    def __init__(self):
        self.ts = 0
        self.type = 0
        self.id = 0
        self.seq = 0

def icmp_rtt(ping):
    # TODO: verify the packet format, be sure the file is well formated
    pcap_type = ETHERNET_II
    f = open('i.pcap')
    pcap = dpkt.pcap.Reader(f)
    i = 0
    for ts, buf in pcap:
        i += 1
        #print "%d" %i
        # Distinguish the packet is "Linux cooked captured" or from Ethernet
        # And only decode the IP packets
        if not cmp(buf[2:6], SSL_HEADER):
            # Linux cooked captured
            pcap_type = LINUX_SSL
            eth = dpkt.sll.SLL(buf)
            if eth.ethtype != ETH_TYPE_IP:
                continue
        else:
            # Ethernet
            eth = dpkt.ethernet.Ethernet(buf)
            if eth.type != ETH_TYPE_IP:
                continue 

        ip = eth.data
        if ip.p == IP_PROTO_ICMP:
            icmp = ip.data
            # only handle ECHO and ECHO_REPLY ICMP messages
            if icmp.type == ICMP_ECHOREPLY or icmp.type == ICMP_ECHO:
                #print "ICMP type %d, id %d, seq %d timestamp %f" % (icmp.type, icmp.data.id, icmp.data.seq, ts)
                ping_pkt = pkt_icmp()
                ping_pkt.ts = ts
                ping_pkt.type = icmp.type
                ping_pkt.id = icmp.data.id
                ping_pkt.seq = icmp.data.seq
                ping.append(ping_pkt)
                #print "ICMP type %d, id %d, seq %d timestamp %f" % (ping_pkt.type, ping_pkt.id, ping_pkt.seq, ping_pkt.ts)

    for pkt in ping:
        print "ICMP type %d, id %d, seq %d timestamp %f" % (pkt.type, pkt.id, pkt.seq, pkt.ts)

    # identify the request and response by the id and seq
    for req in ping:
        for rep in ping:
            if rep.id == req.id and rep.seq == req.seq:
                diff = rep.ts - req.ts
                if diff > 0:
                    print "RTT for id %d seq %d: %f" %(req.id, req.seq, diff)

    f.close()

def main():
    print 'Get RTT of ICMP ping'
    pdb.set_trace()
    ping = []
    icmp_rtt(ping)

if __name__ == '__main__':
    main()

# Define the Linux SSL type
# 0: to us, 1: bcast, 2: mcast, 3: other, 4: from us
SSL_TYPE_TO_US = 0
SSL_TYPE_BCAST = 1
SSL_TYPE_MCAST = 2
SSL_TYPE_OTHER = 4
SSL_TYPE_FROM_US = 4

