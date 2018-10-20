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
    timestamp = datetime.date.time.now()
    if result.is_valid():
        print("Last valid input: " + str(datetime.datetime.now()))
        print("Temperature: %d C" % result.temperature)
        print("Humidity: %d %%" % result.humidity)
    with open('temp_log.csv', mode='w') as temp_log:
        temp_writer = csv.writer('temp_log', delimiter=',', quotechar='"')
        temp_writer.writerow([timestamp, result])

    time.sleep(1)

