# Solução - pisca "SOS" em código Morse no LED vermelho
from machine import Pin
import time

led = Pin(25, Pin.OUT)
PONTO, TRACO = 200, 600            # duração em ms

def sinal(duracao):
    led.on()
    time.sleep_ms(duracao)
    led.off()
    time.sleep_ms(200)             # intervalo entre sinais

while True:
    for d in (PONTO, PONTO, PONTO, TRACO, TRACO, TRACO, PONTO, PONTO, PONTO):
        sinal(d)
    time.sleep_ms(1500)            # pausa entre as palavras
