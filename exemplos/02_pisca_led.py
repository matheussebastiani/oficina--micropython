# 02 - Pisca LED (o "Olá, mundo" dos embarcados)
from machine import Pin
import time

led = Pin(2, Pin.OUT)      # LED azul da placa (GPIO2)

while True:
    led.on()               # liga  -> 3,3 V no pino
    time.sleep(0.5)        # espera 500 ms
    led.off()              # desliga -> 0 V no pino
    time.sleep(0.5)
