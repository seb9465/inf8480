#!/usr/bin/python

import helpers


class Machine:
	def __init__(self, name):
		self.name = name

class SubNetwork:
  	def __init__(self, name, number_machines):
	    self.name = name
	    self.subnetIpAddress = helpers.generate_random_subnet_ip()
	    self.number_machines = number_machines
	    self.machines = []
	    for i in range(0, number_machines):
	    	self.machines.append(Machine(self.name + '_' + helpers.generate_random_string(6)))

	def add_machine(self, name):
		self.machines.append(Machine(name))

	
	def print_subnet(self):
		print("-------- {} --------".format(self.name))
		if self.number_machines == 0:
			print(" Vide")
		else:
			print("IP: {}".format(self.subnetIpAddress))
			for machine in self.machines:
				print("\t Machine: {}".format(machine.name))


class Router:
  	def __init__(self, name, status):
	    self.name = name
	    self.status = status

	def print_router(self):
		print("-------- {} --------".format(self.name))
		if self.status == 0:
			print("Aucun routeur")
		else:
			print("Firewall Configuration:")
			print("\t ALLOW ANY ALL ANY ALL TCP")
