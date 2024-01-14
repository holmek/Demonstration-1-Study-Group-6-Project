from machine import Pin
from time import sleep

RED_PIN = 26
led1 = Pin(RED_PIN, Pin.OUT)

Yellow_PIN = 12
led2 = Pin(Yellow_PIN, Pin.OUT)

GREEN_PIN = 13
led3 = Pin(GREEN_PIN, Pin.OUT)

while True:
    led1(1)
    led2(0)
    led3(0)
    sleep(2)  

    led1(0)
    led2(1)
    led3(0)
    sleep(2)  

    led1(0)
    led2(0)
    led3(1)
    sleep(2)  
