# Solução - jogo de reação com bip e LEDs de resultado
from machine import Pin, PWM
import time, random

led      = Pin(2, Pin.OUT)
verde    = Pin(27, Pin.OUT)
vermelho = Pin(25, Pin.OUT)
botao    = Pin(13, Pin.IN, Pin.PULL_UP)
buzzer   = PWM(Pin(18), freq=1000, duty_u16=0)
recorde  = None

def bip(freq=1000, ms=80):
    buzzer.freq(freq)
    buzzer.duty_u16(32768)
    time.sleep_ms(ms)
    buzzer.duty_u16(0)

while True:
    led.off(); verde.off(); vermelho.off()
    time.sleep_ms(random.randint(1500, 5000))
    if botao.value() == 0:
        print("Queimou a largada!")
        bip(200, 400)
        time.sleep(2)
        continue

    led.on()
    bip()                                   # aviso sonoro
    inicio = time.ticks_ms()
    while botao.value() == 1:
        pass
    reacao = time.ticks_diff(time.ticks_ms(), inicio)
    led.off()

    if recorde is None or reacao < recorde:
        recorde = reacao
        verde.on()
        bip(1500, 60); bip(2000, 60)        # som de vitória
        print("NOVO RECORDE:", reacao, "ms")
    else:
        vermelho.on()
        print("Tempo:", reacao, "ms  (recorde:", recorde, "ms)")
    time.sleep(2)
