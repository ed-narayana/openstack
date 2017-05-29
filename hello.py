from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
import requests
import json



app = Flask(__name__)

@app.route("/")
def hello():
    userid = "admin"
    password = "ilkom"
    tenatid = "92824a27836b4311a750484ffa140a6d"
    url = 'http://172.16.160.110:5000/v2.0/tokens'
    headers = {'content-type': 'application/json'}
    payload = {'auth':{'passwordCredentials':{'username': userid, \
        'password':password}, 'tenantId':tenatid}}    
    
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    json_data = r.json()
    r.close()
    
    tokens = json.loads(json.dumps(json_data))
    tokenid = tokens['access']['token']['id']
    #print tokenid
    
    url = 'http://172.16.160.110:35357/v2.0/users'
    headers = {'X-Auth-Token':str(tokenid)}
    r = requests.get(url, headers=headers)
    json_data = r.json()
    print json.dumps(r.json(), sort_keys=True, indent=4, separators=(',', ': '))
    json_data = r.json()
    r.close()
    return render_template('coba.html', json_data = json_data)

@app.route("/create")
def create():
    #user: {
        #email: "new-user@example.com",
        #password: null,
        #enabled: true,
        #name: "new-user",
        #tenantId: "40429f980fac419bbfec372a5607c154"
    #}
    return "Buat mesin" 


if __name__ == "__main__":
    app.run()
