# 05 - PWM: controlando o brilho do LED
from machine import Pin, PWM
import time

led = PWM(Pin(2), freq=1000)        # 1000 Hz

while True:
    for brilho in range(0, 65536, 1024):     # sobe: 0 % -> 100 %
        led.duty_u16(brilho)
        time.sleep_ms(15)
    for brilho in range(65535, -1, -1024):   # desce: 100 % -> 0 %
        led.duty_u16(brilho)
        time.sleep_ms(15)
