# 15 - Quão rápido é o MicroPython? (pisca um pino o mais rápido possível)
from machine import Pin
import time, micropython

p = Pin(25, Pin.OUT)
N = 10_000

def python_puro():
    for _ in range(N):
        p.on()
        p.off()

@micropython.native            # compila para código de máquina
def nativo():
    for _ in range(N):
        p.on()
        p.off()

@micropython.viper             # tipos fixos, acesso direto a registradores
def viper():
    GPIO_OUT_W1TS = ptr32(0x3FF44008)   # registrador "liga bits"
    GPIO_OUT_W1TC = ptr32(0x3FF4400C)   # registrador "desliga bits"
    mask = 1 << 25
    for _ in range(10_000):
        GPIO_OUT_W1TS[0] = mask
        GPIO_OUT_W1TC[0] = mask

for nome, f in (("Python puro", python_puro), ("native", nativo), ("viper", viper)):
    t0 = time.ticks_us()
    f()
    dt = time.ticks_diff(time.ticks_us(), t0)
    print(f"{nome:12s} {dt/N:6.2f} us por ciclo  ->  {N/dt*1000:7.1f} kHz")
