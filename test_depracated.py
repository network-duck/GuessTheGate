import network
import socket
with open("index.html", "r") as f:
    html = f.read()
from machine import Pin

led = Pin(1, Pin.OUT)

# Set up access point
ap = network.WLAN(network.AP_IF)
ap.config(ssid="GuessTheGate", key="LogicIsFun")
ap.active(True)

print("IP: ", ap.ifconfig()[0])

# Set up socket
s = socket.socket()
s.bind(("0.0.0.0", 80))
s.listen(1)

print("Waiting for connections...")

while True:
    client, addr = s.accept()
    print("Connected from", addr)

    request = client.recv(1024).decode()
    print("Request:", request)

    if "GET /toggle" in request:
        led.value(not led.value())
    
    client.send("HTTP/1.1 200 OK\r\n")
    client.send("Content-Type: text/html\r\n\r\n")
    client.send(html)

    client.close()