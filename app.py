from flask import Flask,render_template,url_for,abort,request,redirect
import requests,json
 
app = Flask(__name__)

@app.errorhandler(404)
def not_found(e):
    return render_template("404.html") 

@app.route('/')
def index():
    return render_template('index.html')        

@app.route('/newdevice/<ip>')
def newdevice(ip=None):
    print(ip)
    return "added"

@app.route('/api/v1/update',methods = ['GET','POST'])
def update():
    if request.method=='GET':
        with open('devicesss.json','r') as devices:
            return json.load(devices)
    if request.method == 'POST':
        if not request.json:
            abort(400)
        req_data=request.json
        #print(req_data)
        node_number=int(req_data['node'][-1])
        with open('devicesss.json','r') as devices:
            devices_json=json.load(devices)
            device=devices_json['nodes'][node_number]
        try:
            url=f"http://{device['ip']}/{req_data['status']}" # pin to be added later
            requests.get(url,timeout=3)
            device_status="reachable"
        except:
            device_status= "unreachable"
        if device_status=="reachable":
            devices_json['nodes'][node_number][req_data['pin']]=req_data['status']
        else:
            devices_json['nodes'][node_number][req_data['pin']]="off"
            req_data['status']=device_status
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