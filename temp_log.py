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
    tempf = str((result.temperature * 9/5)+32)
    with open('temp_log.csv', mode='a') as temp_log:
        temp_writer = csv.writer(temp_log, delimiter=',', quotechar='"')
    	if result.is_valid():
        	print("Last valid input: " + str(datetime.datetime.now()))
        	print("Temperature: %d f" % ((result.temperature * 9/5)+32))
        	print("Humidity: %d %%" % result.humidity)
        	temp_writer.writerow([timestamp, tempf + 'f'])
    time.sleep(60)

