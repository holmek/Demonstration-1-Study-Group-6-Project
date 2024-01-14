from machine import Pin
from time import sleep

RED_PIN = 26
led1 = Pin(RED_PIN, Pin.OUT)

Yellow_PIN = 12
led2 = Pin(Yellow_PIN, Pin.OUT)

GREEN_PIN = 13
led3 = Pin(GREEN_PIN, Pin.OUT)

interval = 2.0  

while True:
    led3(1)  
    sleep(interval)
    led3(0)  
    sleep(interval)

    interval -= 0.1 

    if interval < 0.2:
        break  
