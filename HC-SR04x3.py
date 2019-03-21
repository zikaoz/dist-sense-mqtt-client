#Program

import RPi.GPIO as GPIO
import time
import paho.mqtt.client as mqtt

broker_address = "192.168.0.24" # localhost or IP address Digital Ocean
thing_id = "f46e1619-5d6b-4621-9fcf-2a4f5e427264"
thing_key = "60575333-9b7f-49f2-8040-2f9d1ad7dabd"

client = mqtt.Client()
client.username_pw_set(thing_id, thing_key)
client.connect(broker_address)

time.sleep(0.5)

GPIO.setmode(GPIO.BCM)

#Pins connected to the HC-SR04 sensor
iTriggerPin1 = 23               # GPIO OUT pin sensor_1
iEchoPin1    = 24               # GPIO IN pin sensor_1

iTriggerPin2 = 17               # GPIO OUT pin sensor_2
iEchoPin2    = 4                # GPIO IN pin sensor_2

iTriggerPin3 = 25               # GPIO OUT pin sensor_3
iEchoPin3    = 22               # GPIO IN pin sensor_3

GPIO.setup(iTriggerPin1, GPIO.OUT)
GPIO.setup(iEchoPin1, GPIO.IN)

GPIO.output(iTriggerPin1, False)

GPIO.setup(iTriggerPin2, GPIO.OUT)
GPIO.setup(iEchoPin2, GPIO.IN)

GPIO.output(iTriggerPin2, False)

GPIO.setup(iTriggerPin3, GPIO.OUT)
GPIO.setup(iEchoPin3, GPIO.IN)

GPIO.output(iTriggerPin3, False)

time.sleep(0.5)

while True:

# 1st column

        GPIO.output(iTriggerPin1, True)
        time.sleep(0.0001)
        GPIO.output(iTriggerPin1, False)

        while GPIO.input(iEchoPin1) == 0:
                pass
        fPulseStart = time.time()

        while GPIO.input(iEchoPin1) == 1:
                pass
        fPulseEnd = time.time()

        fPulseDuration = fPulseEnd - fPulseStart

        fDistance_1 = round((fPulseDuration * 171.50), 2)

        print ("Column_1:", fDistance_1, "m.")

# 2nd column

        GPIO.output(iTriggerPin2, True)
        time.sleep(0.0001)
        GPIO.output(iTriggerPin2, False)

        while GPIO.input(iEchoPin2) == 0:
                pass
        fPulseStart = time.time()

        while GPIO.input(iEchoPin2) == 1:
                pass
        fPulseEnd = time.time()

        fPulseDuration = fPulseEnd - fPulseStart

        fDistance_2 = round((fPulseDuration * 171.50), 2)

        print ("Column_2:", fDistance_2, "m.")

# 3rd column

        GPIO.output(iTriggerPin3, True)
        time.sleep(0.0001)
        GPIO.output(iTriggerPin3, False)

        while GPIO.input(iEchoPin3) == 0:
                pass
        fPulseStart = time.time()

        while GPIO.input(iEchoPin3) == 1:
                pass
        fPulseEnd = time.time()

        fPulseDuration = fPulseEnd - fPulseStart
	
	fDistance_3 = round((fPulseDuration * 171.50), 2)

        print ("Column_3:", fDistance_3, "m.")

# Send SENML message

        client.publish(topic = "channels/791ef435-9bbe-4c9e-b502-a482ebf6fed1/messages", payload = "[{\"n\":\"column_1\",\"v\":" + str(fDistance_1) + "}, {\"n\":\"column_2\",\"v\":" + str(fDistance_2) + "}, {\"n\":\"column_3\",\"v\":" + str(fDistance_3) + "}]") 

        time.sleep(1)

GPIO.cleanup()

