# 12 - Procurando redes Wi-Fi
import network

wlan = network.WLAN(network.WLAN.IF_STA)   # modo cliente
wlan.active(True)

print("Procurando redes...")
redes = wlan.scan()          # cada rede é uma tupla com várias informações

for rede in redes:
    nome = rede[0].decode()  # posição 0: nome da rede
    sinal = rede[3]          # posição 3: força do sinal (dBm)
    print(sinal, "dBm", nome)
