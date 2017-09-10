import RPi.GPIO as GPIO
import sys
from time import sleep


ident = int(sys.argv[1])
value = int(sys.argv[2])

GPIO.setmode(GPIO.BCM)

dic = [[17, 27], [15, 18], [27, 22]]

pair = dic[ident-1]
print(pair)

if value == 0:
    pin = pair[1]
elif value == 1:
    pin = pair[0]

print(pin)
GPIO.setup(pin, GPIO.OUT)

GPIO.output(pin, GPIO.LOW)
sleep(0.5)
GPIO.output(pin, GPIO.HIGH)
