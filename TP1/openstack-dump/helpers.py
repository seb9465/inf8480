#!/usr/bin/python

import random
import string
import socket
import struct
from netaddr import IPNetwork

def at_lest_one_true():
	l = [(1,1), (1,0), (0,1)]
	return random.choice(l)

def complete_missing_values(mydict):
    if mydict['d'] == 'x' and mydict['e'] == 'x':
    	val = at_lest_one_true()
    	mydict['d'] = val[0]
    	mydict['e'] = val[1]
    if mydict['f'] == 'x' and mydict['g'] == 'x':
    	val = at_lest_one_true()
    	mydict['f'] = val[0]
    	mydict['g'] = val[1]

def generate_random_string(length):
	random_str = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(length)])
	return random_str


def generate_random_subnet_ip():
	ip = socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))
	ipnetwork_struct = IPNetwork('{}/23'.format(ip))
	return str(ipnetwork_struct[0])+"/23"