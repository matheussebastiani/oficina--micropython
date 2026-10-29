# 09 - Timers: várias tarefas "ao mesmo tempo", sem sleep()
from machine import Pin, Timer

led_placa = Pin(2, Pin.OUT)
led_verde = Pin(19, Pin.OUT)

def pisca_rapido(t):
    led_placa.value(not led_placa.value())

def pisca_lento(t):
    led_verde.value(not led_verde.value())

t0 = Timer(0)
t1 = Timer(1)
t0.init(period=200,  mode=Timer.PERIODIC, callback=pisca_rapido)
t1.init(period=1000, mode=Timer.PERIODIC, callback=pisca_lento)

print("Timers rodando! O REPL continua livre.")
print("Para parar: t0.deinit(); t1.deinit()")
