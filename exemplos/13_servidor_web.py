# 13 - Servidor web: controle o LED pelo celular
import network, socket
from machine import Pin

led = Pin(2, Pin.OUT)

# A ESP32 cria sua PRÓPRIA rede Wi-Fi (modo Access Point)
ap = network.WLAN(network.WLAN.IF_AP)
ap.active(True)
mac = ap.config("mac")
nome = "ESP32-%02X%02X" % (mac[-2], mac[-1])   # nome único por placa
ap.config(essid=nome, password="senainfo",
          security=network.AUTH_WPA2_PSK)
print("Conecte-se na rede", nome, "(senha: senainfo)")
print("e abra http://" + ap.ifconfig()[0])

PAGINA = """<!DOCTYPE html><html><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>ESP32</title><style>
body{font-family:sans-serif;text-align:center;background:#f4f4f4;margin-top:40px}
a{display:inline-block;padding:18px 36px;margin:10px;font-size:22px;
color:#fff;border-radius:12px;text-decoration:none}
.on{background:#2e9e45}.off{background:#d7262e}</style></head><body>
<h1>Controle do LED</h1><p>O LED est&aacute; <b>%s</b></p>
<a class="on" href="/on">LIGAR</a><a class="off" href="/off">DESLIGAR</a>
</body></html>"""

srv = socket.socket()
srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
srv.bind(("0.0.0.0", 80))
srv.listen(2)

while True:
    cliente, endereco = srv.accept()
    pedido = cliente.recv(1024).decode()
    caminho = pedido.split(" ")[1] if " " in pedido else "/"
    print(endereco[0], "pediu", caminho)

    if caminho == "/on":
        led.on()
    elif caminho == "/off":
        led.off()

    estado = "LIGADO" if led.value() else "DESLIGADO"
    cliente.send("HTTP/1.0 200 OK\r\n"
                 "Content-Type: text/html\r\n\r\n")
    cliente.send(PAGINA % estado)
    cliente.close()
