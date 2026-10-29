# 07 - ADC: lendo um potenciômetro e controlando o brilho
from machine import Pin, ADC, PWM
import time

pot = ADC(Pin(4))                  # GPIO4: entrada analógica (ADC2)
pot.atten(ADC.ATTN_11DB)           # lê de 0 a 3,3 V
led = PWM(Pin(2), freq=1000)

while True:
    valor = pot.read_u16()         # 0 ... 65535
    led.duty_u16(valor)            # brilho acompanha o potenciômetro
    print(valor)                   # o Plotter do Thonny desenha isso!
    time.sleep_ms(100)
