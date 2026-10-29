# Solução - página web com os 3 LEDs e a leitura do potenciômetro
import network, socket
from machine import Pin, ADC

# lista de pares (nome, pino): mantém a ordem dos botões na página
leds = [("vermelho", Pin(25, Pin.OUT, value=0)),
        ("amarelo",  Pin(26, Pin.OUT, value=0)),
        ("verde",    Pin(27, Pin.OUT, value=0))]
pot = ADC(Pin(34))
pot.atten(ADC.ATTN_11DB)

ap = network.WLAN(network.WLAN.IF_AP)
ap.active(True)
mac = ap.config("mac")
nome = "ESP32-%02X%02X" % (mac[-2], mac[-1])
ap.config(essid=nome, password="senainfo",
          security=network.AUTH_WPA2_PSK)
print("Rede:", nome, " ->  http://" + ap.ifconfig()[0])

def pagina():
    botoes = ""
    for cor, pino in leds:
        estado = "ON" if pino.value() else "off"
        botoes += '<p><a href="/%s">%s</a> %s</p>' % (cor, cor.upper(), estado)
    volts = pot.read_uv() / 1_000_000
    return ("<!DOCTYPE html><html><head><meta charset='utf-8'>"
            "<meta name='viewport' content='width=device-width'>"
            "<meta http-equiv='refresh' content='3;url=/'>"   # atualiza a cada 3 s
            "<style>body{font-family:sans-serif;text-align:center}"
            "a{display:inline-block;width:160px;padding:14px;margin:4px;"
            "background:#279c38;color:#fff;border-radius:10px;"
            "text-decoration:none}</style></head><body>"
            "<h1>Semáforo web</h1>" + botoes +
            "<h2>Potenciômetro: %.2f V</h2></body></html>" % volts)

srv = socket.socket()
srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
srv.bind(("0.0.0.0", 80))
srv.listen(2)

while True:
    cliente, _ = srv.accept()
    pedido = cliente.recv(1024).decode()
    caminho = pedido.split(" ")[1] if " " in pedido else "/"
    for cor, pino in leds:
        if caminho == "/" + cor:
            pino.value(not pino.value())           # inverte o LED clicado
    cliente.send("HTTP/1.0 200 OK\r\nContent-Type: text/html\r\n\r\n")
    cliente.send(pagina())
    cliente.close()
