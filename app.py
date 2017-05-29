from flask import Flask, render_template, request, session, g, redirect, url_for, abort, flash
import requests
import json
import time

app = Flask(__name__)

@app.route("/")
def new():

	return render_template('index.html')

def create_tenant():
	
	userid = "admin"
	password = "ilkom"
	tenatid = "92824a27836b4311a750484ffa140a6d" 
	url = 'http://172.16.160.110:5000/v2.0/tokens'
	headers = {'content-type': 'application/json'}
	payload = {'auth':{'passwordCredentials':{'username': userid, 'password':password}, 'tenantId':tenatid}}
	r = requests.post(url, data=json.dumps(payload), headers=headers)
	json_data = r.json()
	r.close()
	tokens = json.loads(json.dumps(json_data))
	#print tokens
	tokenid = tokens['access']['token']['id']

	#print tokenid
	url = 'http://172.16.160.110:35357/v2.0/tenants'
	headers = {'X-Auth-Token':str(tokenid)}
	r = requests.post(url, data=json.dumps({"tenant":{"name":"tendy4", "description":None, "enabled":True}}), headers=headers)
	#print r
	#r = requests.get(url, headers=headers)
	json_data = r.json()
	print json.dumps(r.json(), sort_keys=True, indent=4, separators=(',', ': '))
	json_data = r.json()
	r.close()
	tenant1 = json.loads(json.dumps(json_data))
	#print tenant1
	tenantid = tenant1['tenant']['id']

	url = 'http://172.16.160.110:35357/v2.0/users'
	headers = {'X-Auth-Token':str(tokenid)}
	r = requests.post(url, data=json.dumps({"user": { "email": "tendy.ariyanto99@gmail.com", "password": '','name': 'tendy4', 'tenantid':str(tenantid) }}), headers=headers)
	#print r
	#r = requests.get(url, headers=headers)
	json_data = r.json()
	#print json.dumps(r.json(), sort_keys=True, indent=4, separators=(',', ': '))
	json_data = r.json()
	r.close()
	user = json.loads(json.dumps(json_data))
	#print tenant1
	userid = user['user']['id']

	url = 'http://172.16.160.110:35357/v2.0/users' 
	#print url
	headers = {'X-Auth-Token':str(tokenid)}
	r = requests.get(url,{"name":"admin"}, headers=headers)
	#print r
	#r = requests.get(url, headers=headers)
	json_data = r.json()
	print json.dumps(r.json(), sort_keys=True, indent=4, separators=(',', ': '))
	json_data = r.json()
	r.close()
	useradmin = json.loads(json.dumps(json_data))
	#print tenant1
	useradminid = useradmin['user']['id']

	url = 'http://172.16.160.110:35357/v2.0/OS-KSADM/roles' 
	#print url
	headers = {'X-Auth-Token':str(tokenid)}
	r = requests.get(url, headers=headers)
	#print r
	#r = requests.get(url, headers=headers)
	json_data = r.json()
	print json.dumps(r.json(), sort_keys=True, indent=4, separators=(',', ': '))
	json_data = r.json()
	r.close()
	adminrole_ = json.loads(json.dumps(json_data))
	#print tokens
	adminrole_id = adminrole_['roles'][2]['id']
	memberrole_ = json.loads(json.dumps(json_data))
	#print tokens
	memberrole_id = memberrole_['roles'][1]['id']
	anotherrole_ = json.loads(json.dumps(json_data))
	#print tokens
	anotherrole_id = anotherrole_['roles'][0]['id']

	url = 'http://172.16.160.110:35357/v2.0/tenants/%s/users/%s/roles/OS-KSADM/%s' %(tenantid,useradminid,adminrole_id)
	#print url
	headers = {'X-Auth-Token':str(tokenid)}
	r = requests.put(url, headers=headers)
	#print r
	#r = requests.get(url, headers=headers)
	json_data = r.json()
	#print json.dumps(r.json(), sort_keys=True, indent=4, separators=(',', ': '))
	json_data = r.json()
	r.close()

	url = 'http://172.16.160.110:35357/v2.0/tenants/%s/users/%s/roles/OS-KSADM/%s' %(tenantid,userid,memberrole_id)
	headers = {'X-Auth-Token':str(tokenid)}
	r = requests.put(url, headers=headers)
	#print r
	#r = requests.get(url, headers=headers)
	json_data = r.json()
	#print json.dumps(r.json(), sort_keys=True, indent=4, separators=(',', ': '))
	json_data = r.json()
	r.close()

	url = 'http://172.16.160.110:35357/v2.0/tenants/%s/users/%s/roles/OS-KSADM/%s' %(tenantid,userid,anotherrole_id)
	headers = {'X-Auth-Token':str(tokenid)}
	r = requests.put(url, headers=headers)
	#print r
	#r = requests.get(url, headers=headers)
	json_data = r.json()
	#print json.dumps(r.json(), sort_keys=True, indent=4, separators=(',', ': '))
	json_data = r.json()
	r.close()
	return tenantid

#def create_vm():
	
	
	#print tokens
	#return

@app.route("/spawn")
def spawn():
	tenantid1 = create_tenant()
	#create_vm()
	userid = "admin"
	password = "ilkom"
	tenatid = tenantid1 #tenant admin
	url = 'http://172.16.160.110:5000/v2.0/tokens'
	headers = {'content-type': 'application/json'}
	payload = {'auth':{'passwordCredentials':{'username': userid, 'password':password}, 'tenantId':str(tenatid)}}
	r = requests.post(url, data=json.dumps(payload), headers=headers)
	json_data = r.json()
	r.close()
	tokens = json.loads(json.dumps(json_data))
	#print tokens
	tokenid = tokens['access']['token']['id']

	url = 'http://172.16.160.110:9696/v2.0/networks'
	headers = {'X-Auth-Token':str(tokenid)}
	r = requests.post(url, data=json.dumps({"network": {"name": "tendy_network", "admin_state_up": True}}), headers=headers)
	#print r
	json_data = r.json()
	print json.dumps(r.json(), sort_keys=True, indent=4, separators=(',', ': '))
	json_data = r.json()
	r.close()
	network_ = json.loads(json.dumps(json_data))
	network_id = network_['network']['id']

	url = 'http://172.16.160.110:9696/v2.0/subnets'
	headers = {'X-Auth-Token':str(tokenid)}
	r = requests.post(url, data=json.dumps({"subnet": {"name":"tendy_subnet" ,"network_id": str(network_id), "ip_version": 4, "cidr": "192.168.1.0/24"}}), headers=headers)
	print r
	json_data = r.json()
	print json.dumps(r.json(), sort_keys=True, indent=4, separators=(',', ': '))
	json_data = r.json()
	r.close()
	subnet_ = json.loads(json.dumps(json_data))
	subnet_id = subnet_['subnet']['id']

	url = 'http://172.16.160.110:9696/v2.0/floatingips'
	headers = {'X-Auth-Token':str(tokenid)}
	r = requests.get(url, headers=headers)
	print r
	json_data = r.json()
	print json.dumps(r.json(), sort_keys=True, indent=4, separators=(',', ': '))
	json_data = r.json()
	r.close()
	floatingip_ = json.loads(json.dumps(json_data))
	floatingip_id = floatingip_['floatingips'][1]['floating_network_id']

	url = 'http://172.16.160.110:9696/v2.0/routers'
	headers = {'X-Auth-Token':str(tokenid)}
	r = requests.post(url, data=json.dumps({"router": {"name": "tendy_router","external_gateway_info": {"network_id": str(floatingip_id), "enable_snat": True},"admin_state_up": True}}), headers=headers)
	print r
	json_data = r.json()
	print json.dumps(r.json(), sort_keys=True, indent=4, separators=(',', ': '))
	json_data = r.json()
	r.close()
	router_ = json.loads(json.dumps(json_data))
	router_id = router_['router']['id']

	url = 'http://172.16.160.110:9696/v2.0/routers/%s/add_router_interface' %(router_id)
	headers = {'X-Auth-Token':str(tokenid)}
	r = requests.put(url, data=json.dumps({"subnet_id": str(subnet_id)}), headers=headers)
	json_data = r.json()
	print json.dumps(r.json(), sort_keys=True, indent=4, separators=(',', ': '))
	json_data = r.json()
	r.close()

	url = 'http://172.16.160.110:8774/v2/%s/flavors' %(tenatid)
	#print url
	headers = {'X-Auth-Token'	:str(tokenid)}
	r = requests.get(url, headers=headers)
	#print r
	#r = requests.get(url, headers=headers)
	json_data = r.json()
	print json.dumps(r.json(), sort_keys=True, indent=4, separators=(',', ': '))
	json_data = r.json()
	r.close()
	flavor_ = json.loads(json.dumps(json_data))
	#print tokens
	flavor_id = flavor_['flavors'][0]['id']

	url = 'http://172.16.160.110:9292/v2/images' 
	#print url
	headers = {'X-Auth-Token':str(tokenid)}
	r = requests.get(url, headers=headers)
	#print r
	#r = requests.get(url, headers=headers)
	json_data = r.json()
	print json.dumps(r.json(), sort_keys=True, indent=4, separators=(',', ': '))
	json_data = r.json()
	r.close()
	image_ = json.loads(json.dumps(json_data))
	#print tokens
	image_id = image_['images'][4]['id']

	url = 'http://172.16.160.110:8774/v2/%s/servers' %(tenatid)
	headers = {'content-type': 'application/json','X-Auth-Token':str(tokenid)}
	crt = {'server':{'name': "zemble", 'flavorRef': str(flavor_id), 'imageRef': str(image_id), 'adminPass': password, 'key_name':'keyspair'}}
	r = requests.post(url, data=json.dumps(crt), headers=headers)
	#t = requests.get(url, headers=headers)
	json_data = r.json()
	print json.dumps(r.json(), sort_keys=True, indent=4, separators=(',', ': '))
	json_data = r.json()
	r.close()
	server_ = json.loads(json.dumps(json_data))
	#print tokens
	server_id = server_['server']['id']

	url = 'http://172.16.160.110:8774/v2/%s/os-floating-ip-pools' %(tenatid)
	headers = {'content-type': 'application/json','X-Auth-Token':str(tokenid)}
	r = requests.get(url, headers=headers)
	#t = requests.get(url, headers=headers)
	json_data = r.json()
	print json.dumps(r.json(), sort_keys=True, indent=4, separators=(',', ': '))
	json_data = r.json()
	r.close()
	floatings_ = json.loads(json.dumps(json_data))
	#print tokens
	floatings_name = floatings_['floating_ip_pools'][0]['name']	

	url = 'http://172.16.160.110:8774/v2/%s/os-floating-ips' %(tenatid)
	headers = {'content-type': 'application/json','X-Auth-Token':str(tokenid)}
	r = requests.post(url, data=json.dumps({"pool": str(floatings_name)}), headers=headers)
	#t = requests.get(url, headers=headers)
	json_data = r.json()
	print json.dumps(r.json(), sort_keys=True, indent=4, separators=(',', ': '))
	json_data = r.json()
	r.close()
	floatingss_ = json.loads(json.dumps(json_data))
	#print tokens
	floatingss_ip = floatingss_['floating_ip']['ip']
	print floatingss_ip

	time.sleep(10)
	url = 'http://172.16.160.110:8774/v2/%s/servers/%s' %(tenatid,server_id)
	headers = {'content-type': 'application/json','X-Auth-Token':str(tokenid)}
	r = requests.get(url, headers=headers)
	json_data = r.json()
	print json.dumps(r.json(), sort_keys=True, indent=4, separators=(',', ': '))
	json_data = r.json()
	r.close()
	server_ = json.loads(json.dumps(json_data))
	#print tokens
	server_ip = server_['server']['addresses']['tendy_network'][0]['addr']
	print server_ip

	url = 'http://172.16.160.110:8774/v2/%s/servers/%s/action' %(tenatid,server_id)
	headers = {'content-type': 'application/json','X-Auth-Token':str(tokenid)}
	r = requests.post(url, data=json.dumps({"addFloatingIp" : {"address": str(floatingss_ip), "fixed_address": str(server_ip) }}), headers=headers)
	
	return render_template('sukses.html')
	#return render_template('sukses.html', json_data = json_data)

if __name__ == '__main__':
	app.run()