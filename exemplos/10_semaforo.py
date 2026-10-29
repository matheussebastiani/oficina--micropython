# 10 - Semáforo com três LEDs e botão de pedestre
from machine import Pin
import time

vermelho = Pin(25, Pin.OUT)
amarelo  = Pin(26, Pin.OUT)
verde    = Pin(27, Pin.OUT)
botao    = Pin(13, Pin.IN, Pin.PULL_UP)

def acende(cor):
    for led in (vermelho, amarelo, verde):
        led.off()
    cor.on()

def espera(segundos):
    # espera em passos de 10 ms, olhando o botão a cada passo
    for i in range(segundos * 100):
        if botao.value() == 0:
            print("Pedestre pediu passagem!")
            return
        time.sleep_ms(10)

while True:
    acende(verde)
    espera(5)      # ou menos, se apertarem
    acende(amarelo)
    time.sleep(2)
    acende(vermelho)
    time.sleep(4)
