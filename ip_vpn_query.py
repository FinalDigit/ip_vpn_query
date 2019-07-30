#!/usr/bin/python
import sys
import urllib.request
import json
import requests

file = sys.argv[1]
ip_list = []
with open (file, 'r') as f:
	for ip in f.read().splitlines(): ip_list.append(ip)

def Lookup(ip):
	
	api = '<API KEY>'
	response = urllib.request.Request("http://v2.api.iphub.info/ip/{}".format(ip))
	response.add_header("X-Key", api)
	
	try:
		response = json.loads(urllib.request.urlopen(response).read().decode())
		#print(response)
	except:
		return False # In the case of an error, pass all IP's to avoid blocking innocents

	#return response.get("block") # Defaults to None if failed to get block value
	return response # Defaults to None if failed to get block value


for ip in ip_list:	
	results = Lookup(ip)
	print(json.dumps(results, indent=2))
