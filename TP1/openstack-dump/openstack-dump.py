#!/usr/bin/python

import json
import subprocess

dump = dict();
serversdetails = dict();
networksdetails = dict();
subnetsdetails = dict();
routersdetails = dict();


print("Retrieving server list")

servers = subprocess.check_output(['openstack', 'server', 'list','-f', 'json'])
servers = json.loads(servers)
dump["serverlist"] = servers

print("Retrieving server info")

for server in servers:
    servername = server["Name"]
    serv_detail = subprocess.check_output(['openstack', 'server', 'show', servername , '-f', 'json'])
    serv_detail = json.loads(serv_detail)
    serversdetails[servername] = serv_detail

dump["serversdetails"] = serversdetails

print("Retrieving network list")

networks = subprocess.check_output(['openstack', 'network', 'list','-f', 'json'])
networks = json.loads(networks)
dump["networklist"] = networks

print("Retrieving network info")

for network in networks:
    networkname = network["Name"]
    net_detail = subprocess.check_output(['openstack', 'network', 'show', networkname , '-f', 'json'])
    net_detail = json.loads(net_detail)
    networksdetails[networkname] = net_detail

dump["networksdetails"] = networksdetails

print("Retrieving subnet list")

subnets = subprocess.check_output(['openstack', 'subnet', 'list','-f', 'json'])
subnets = json.loads(subnets)
dump["subnetlist"] = subnets

print("Retrieving subnet info")

for subnet in subnets:
    subnetid = subnet["ID"]
    subnet_detail = subprocess.check_output(['openstack', 'subnet', 'show', subnetid , '-f', 'json'])
    subnet_detail = json.loads(subnet_detail)
    subnetsdetails[subnetid] = subnet_detail

dump["subnetsdetails"] = subnetsdetails

print("Retrieving router list")

routers = subprocess.check_output(['openstack', 'router', 'list','-f', 'json'])
routers = json.loads(routers)
dump["routerlist"] = routers

print("Retrieving router info")

for router in routers:
    routername = router["Name"]
    router_detail = subprocess.check_output(['openstack', 'router', 'show', routername , '-f', 'json'])
    router_detail = json.loads(router_detail)
    routersdetails[routername] = router_detail

dump["routersdetails"] = routersdetails

#print("Retrieving port list")

#ports = subprocess.check_output(['neutron', 'port-list', '-c', 'device_id', '-c', 'fixed_ips', '-c', 'device_owner', '-c', 'network_id', '-f', 'json'])
#ports = json.loads(ports)
#dump["ports"] = ports


f1=open('./full-dump', 'w+')
f1.write(json.dumps(dump, indent=4, sort_keys=True))
f1.close()

print("Finished")

