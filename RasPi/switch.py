from gpiozero import *
import sys
from time import sleep


ident = sys.argv[1]
value = int(sys.argv[2])

"""print(ident)
print(value)"""

dic =[[11, 13], [15, 18], [27, 22] ]

pair = dic[int(ident)-1]
print(pair)

if value == 0:
    print(pair[1])
    pin = LED(pair[1])
elif value == 1:
    print(pair[0])
    pin = LED(pair[0])

pin.off()

pin.on()
sleep(10)
pin.off()
