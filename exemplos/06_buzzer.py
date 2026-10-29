# 06 - Tocando notas em um buzzer passivo com PWM
from machine import Pin, PWM
import time

buzzer = PWM(Pin(18), freq=440, duty_u16=0)

NOTAS = {"C": 262, "D": 294, "E": 330, "F": 349,
         "G": 392, "A": 440, "B": 494, "-": 0}

musica = "C D E F - F F - C D C D - D D - C G F E - E E - C D E F - F F"

def tocar(nota, duracao_ms=200):
    if NOTAS[nota] == 0:
        buzzer.duty_u16(0)              # pausa = silêncio
    else:
        buzzer.freq(NOTAS[nota])
        buzzer.duty_u16(32768)          # 50 % de duty -> onda quadrada
    time.sleep_ms(duracao_ms)
    buzzer.duty_u16(0)
    time.sleep_ms(30)

for n in musica.split():
    tocar(n)
buzzer.deinit()
print("Fim da música!")
