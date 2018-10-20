import RPi.GPIO as GPIO
import RPi.GPIO as GPIO
import dht11
import time
import datetime
import csv

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using pin 4
instance = dht11.DHT11(pin=4)

while True:
    result = instance.read()
    timestamp = datetime.datetime.now()
    tempf = (result.temperature * 9/5)+32
    if result.is_valid():
        print("Last valid input: " + str(datetime.datetime.now()))
        print("Temperature: %d f" % ((result.temperature * 9/5)+32))
        print("Humidity: %d %%" % result.humidity)
   	with open('temp_log1.csv', mode='w') as temp_log:
        	temp_writer = csv.writer(temp_log, delimiter=',', quotechar='"')
        	for row in temp_log:
			timestamp.append(row[0])
			tempf.append(row[1])
    time.sleep(5)

