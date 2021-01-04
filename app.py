from flask import Flask,render_template,url_for
import requests
 
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html',res="")

#internal led routes
@app.route('/led/<led>')
def indexafter(led=None):
    res=""
    try:
        node_ip="192.168.1.5:301"
        url=f"http://{node_ip}/{led}"
        res=requests.get(url,timeout=5).text
        #img="https://media.tenor.com/images/cb59b63eb4fe2e3336e4c1fd2ae527b1/tenor.gif"
        #img="https://www.memeatlas.com/images/pepes/pepe-crying-eyes-closed-meme.gif"
    except:
        res="invalid device"
    return res

if __name__=="__main__":
    app.run(host='0.0.0.0',port=5000)