# 11 - Desafio: jogo de tempo de reação
from machine import Pin
import time, random

led   = Pin(2, Pin.OUT)
botao = Pin(13, Pin.IN, Pin.PULL_UP)
recorde = None

print("Aperte o botão assim que o LED acender!")

while True:
    led.off()
    time.sleep_ms(random.randint(1500, 5000))   # espera aleatória

    if botao.value() == 0:
        print("Queimou a largada!")
        time.sleep(2)
        continue

    led.on()
    inicio = time.ticks_ms()
    while botao.value() == 1:                    # espera o aperto
        pass
    reacao = time.ticks_diff(time.ticks_ms(), inicio)
    led.off()

    if recorde is None or reacao < recorde:
        recorde = reacao
        print("NOVO RECORDE:", reacao, "ms")
    else:
        print("Tempo:", reacao, "ms   (recorde:", recorde, "ms)")
    time.sleep(2)
