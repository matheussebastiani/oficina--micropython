# 14 - Testando o Plotter do Thonny (Visualizar > Plotter)
import math, time

t = 0
while True:
    seno = math.sin(t)
    cosseno = math.cos(t) * 0.5
    print(round(seno, 3), round(cosseno, 3))   # cada número vira uma linha
    t += 0.15
    time.sleep_ms(50)
