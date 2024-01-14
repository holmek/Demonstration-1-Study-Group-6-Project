from machine import Pin
from time import sleep

led1 = Pin(26, Pin.OUT, value =0)

pb1 = Pin(4, Pin.IN)

while True:
    print("knap værdi: ", pb1.value())
    if led1.value() == pb1.value():
        led1.value(1)
        sleep(0.1)
    else:
        led1.value(0)
        sleep(0.1)
