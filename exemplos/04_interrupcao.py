# 04 - Interrupção: o hardware avisa quando o botão é pressionado
from machine import Pin
import time

led   = Pin(2, Pin.OUT)
botao = Pin(13, Pin.IN, Pin.PULL_UP)
contador = 0
ultimo = 0

def ao_apertar(pino):
    global contador, ultimo
    agora = time.ticks_ms()
    if time.ticks_diff(agora, ultimo) > 200:   # ignora repiques (debounce)
        contador += 1
        led.value(not led.value())             # inverte o LED
        ultimo = agora

botao.irq(trigger=Pin.IRQ_FALLING, handler=ao_apertar)

while True:                                    # o laço principal fica livre!
    print("Apertos:", contador)
    time.sleep(1)
