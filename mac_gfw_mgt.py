# -*- coding: utf-8 -*-
# manage the socket5 proxy on MAC
# TODO
# - get status of autossh and proxy status
# - echo the info about proxy to file
# - show the proxy status on the bar
# - restart the autossh task

import sys
import psutil
# using psutil 3.2.2. 
# The higher version will have "ZombieProcess process still exists but it's a zombie" issue.
# http://stackoverflow.com/questions/34081476/zombie-process-running-xlwings
import pdb

PROCNAME = "autossh"
PORT = 1080

def check_listening_port(port):
    """Return True if the given TCP port is busy and in LISTEN mode."""
    for conn in psutil.net_connections(kind='tcp'):
        if conn.laddr[1] == port:
            if conn.status == psutil.CONN_LISTEN or conn.status == psutil.CONN_ESTABLISHED:
                return True
    return False

for proc in psutil.process_iter():
    if proc.name() == PROCNAME:
        print "Task %s is running." % proc.name()
        print proc.connections()

if check_listening_port(PORT):
    print "Connection is OK"
else:
    print "Connection is NOK"

# periodically report connections
# any way to test translate delay?
# curl --socks5 127.0.0.1:1080 --connect-timeout 10 google.com

