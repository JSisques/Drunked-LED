import RPi.GPIO as GPIO
import time
from flask import Flask, render_template, request
app = Flask(__name__)
red = 38
green = 40
blue = 37
white = [40, 38, 37]
GPIO.setmode(GPIO.BOARD)
relay = white
for x in relay:
    GPIO.setup(x, GPIO.OUT)

for x in relay:
    GPIO.output(x, GPIO.LOW)

@app.route("/")
def index():
    return render_template('index.html')
@app.route("/<deviceName>/")
def action(deviceName):
    if deviceName != 'white':
        if deviceName == 'green':
            relay = green
        if deviceName == 'blue':
            relay = blue
        if deviceName == 'red':
            relay = red
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(relay, GPIO.OUT)
        GPIO.output(relay, GPIO.HIGH)
        time.sleep(5)
        GPIO.output(relay, GPIO.LOW)
    else:
        relay = white
        for x in relay:
            GPIO.setmode(GPIO.BOARD)
            GPIO.setup(x, GPIO.OUT)
            GPIO.output(x, GPIO.HIGH)
        time.sleep(5)
        for x in relay:
            GPIO.output(x, GPIO.LOW)
    return render_template('index.html')
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
