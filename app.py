from flask import Flask,render_template,url_for,abort,request,redirect
import requests,json
 
app = Flask(__name__)

@app.errorhandler(404)
def not_found(e):
    return render_template("404.html") 

@app.route('/')
def index():
    return render_template('index.html')

#internal led routes
@app.route('/led/<led>')
def device(led=None):
    if led not in ("on","off","sync"): #valid urls
        abort(404)
    try:
        node_code="node1"
        node=get_node_status(node_code)
        if led=='sync':
            return node['led']
        url=f"http://{node['ip']}/{led}"
        res=requests.get(url,timeout=3)
        update_node(node_code,'led',res.text.lower())
        return res.text.lower()
    except:
        update_node(node_code,'led','off')
        return "invalid device"

@app.route('/newdevice/<ip>')
def newdevice(ip=None):
    print(ip)
    return "added"


@app.route('/api/v1/update',methods = ['POST'])
def update():
    if not request.json:
        abort(400)
    req_data=request.json
    print(req_data)
    node_number=int(req_data['node'][-1])
    with open('devicesss.json','r') as devices:
        devices_json=json.load(devices)
        device=devices_json['nodes'][node_number]
    try:
        url=f"http://{device['ip']}/{req_data['status']}"
        requests.get(url,timeout=3)
    except:
        return "invalid device"
    devices_json['nodes'][node_number][req_data['pin']]=req_data['status']
    with open('devicesss.json','w') as devices:
        json.dump(devices_json, devices)
    return req_data['status']


def get_node_status(node):
    with open('devices.json', 'r') as devices:
        return json.load(devices)[node]

def update_node(node,pin,status):
    with open("devices.json", "r") as jsonFile:
        data = json.load(jsonFile)
    data[node][pin] = status
    with open("devices.json", "w") as jsonFile:
        json.dump(data, jsonFile)    
        

if __name__=="__main__":
    app.run(host='0.0.0.0',port=5000)