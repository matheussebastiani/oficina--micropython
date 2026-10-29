# 03 - Lendo um botão (entrada digital com pull-up interno)
from machine import Pin
import time

led   = Pin(2, Pin.OUT)
botao = Pin(13, Pin.IN, Pin.PULL_UP)   # solto = 1, apertado = 0

while True:
    if botao.value() == 0:             # apertado (ligado ao GND)
        led.on()
    else:
        led.off()
    time.sleep_ms(20)                  # pequeno atraso (debounce simples)
