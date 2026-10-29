# 08 - Sensor de toque capacitivo (sem nenhum componente extra!)
from machine import Pin, TouchPad
import time

toque = TouchPad(Pin(4))     # basta um fio (jumper) no GPIO4
led = Pin(2, Pin.OUT)

LIMIAR = 300                 # ajuste olhando os valores no Plotter

while True:
    valor = toque.read()     # valor cai quando você encosta o dedo
    led.value(valor < LIMIAR)
    print(valor)
    time.sleep_ms(100)
