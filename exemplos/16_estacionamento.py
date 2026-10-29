# 16 - Prática final: sensor de estacionamento (Pin + PWM + ADC)
from machine import Pin, ADC, PWM
import time

pot      = ADC(Pin(4))          # "distância" do obstáculo
pot.atten(ADC.ATTN_11DB)        # lê de 0 a 3,3 V
verde    = PWM(Pin(19), freq=1000)
vermelho = Pin(21, Pin.OUT)
buzzer   = PWM(Pin(18), freq=2000, duty_u16=0)

def medir():                    # 0 = encostado, 100 = longe
    distancia = 100 - pot.read_u16() * 100 // 65535
    verde.duty_u16(distancia * 655)   # longe = verde forte
    print(distancia)                  # veja no Plotter
    return distancia

def bipe(som_ms, pausa_ms):
    vermelho.on()
    buzzer.duty_u16(32768)      # som
    time.sleep_ms(som_ms)
    vermelho.off()
    buzzer.duty_u16(0)          # silêncio
    time.sleep_ms(pausa_ms)

while True:
    distancia = medir()
    if distancia > 80:          # longe: quieto
        time.sleep_ms(50)
    elif distancia > 10:        # perto: bipes
        bipe(60, distancia * 8)
    else:                       # vai bater!
        bipe(100, 0)
