#Program

import RPi.GPIO as GPIO
import time
import paho.mqtt.client as mqtt

broker_address = "10.241.78.152"	# localhost or IP address
thing_id = "f46e1619-5d6b-4621-9fcf-2a4f5e427264"
thing_key = "60575333-9b7f-49f2-8040-2f9d1ad7dabd"

client = mqtt.Client()
client.username_pw_set(thing_id, thing_key)
client.connect(broker_address)

GPIO.setmode(GPIO.BCM)

#Pins connected to the HC-SR04 sensor
iTriggerPin = 23
iEchoPin    = 24


GPIO.setup(iTriggerPin, GPIO.OUT)
GPIO.setup(iEchoPin, GPIO.IN)

GPIO.output(iTriggerPin, False)
time.sleep(0.5)

while True:
	GPIO.output(iTriggerPin, True)
	time.sleep(0.0001)
	GPIO.output(iTriggerPin, False)

	while GPIO.input(iEchoPin) == 0:
		pass
	fPulseStart = time.time()

	while GPIO.input(iEchoPin) == 1:
		pass
	fPulseEnd = time.time()

	fPulseDuration = fPulseEnd - fPulseStart

	fDistance = round((fPulseDuration * 171.50), 4)

	print ("Distance:", fDistance, "m.")

	client.publish(topic = "channels/791ef435-9bbe-4c9e-b502-a482ebf6fed1/messages", payload = "[{\"n\":\"distance\",\"u\":\"m\",\"v\":" + str(fDistance) + "}]")

	time.sleep(0.5)

GPIO.cleanup()
