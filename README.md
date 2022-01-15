# Smart Home Web Application

## Objective

* Creating a web-application that controls home appliances over the network.
* Making ‘non-smart’ home devices function smartly by attaching a micro-controller
(NodeMCU) to them.

## Hardware Required
* NodeMCU (ESP8266)
* Relay module (4 channel preferred)
* Webcam

## Flow
The flow of the application will be like this
![flow.jpeg](/images/flow.jpeg)

## Installation

* NodeMCU
```bash
4.  const char* ssid = "xxxxx";
5.  const char* password = "xxxxx";
53.  String url = "http://192.168.1.7:5000/newdevice/"; // enter your flask server's local ip
```
change xxxxx in line with your wifi ssid and password
and change line 53 with your server's local ip. \
Don't forget to open the firewall for port 5000. \
Use the Arduino IDE to flash the code to NodeMCU

* Flask server

Run the server using

```bash
pip install -r requirements.txt
export flask_app=app.py
export flask_env=development
python app.py
```
or if using venv
```bash
python -m pip venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export flask_app=app.py
export flask_env=development
python app.py
```

## Usage

1. If a new device is detected its IP will be stored in the [devicesss.json](/devicesss.json) \
![newdev.jpeg](/images/newdev.jpeg)

2. Open the flask WebApp at __localhost:5000__ using any browser. \
You will see UI like this \
![ui.jpeg](/images/ui.jpeg)

3. You can add devicesss manually also in [devicesss.json](/devicesss.json)

Enjoy :)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

