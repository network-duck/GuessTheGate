import network
import socket

class Server:
    def __init__(self, main):
        self.main = main
        self.web()
        self.ap()
        self.socket()

    def web(self):
        with open("web/index.html") as f:
            self.html = f.read()
        with open("web/style.css") as f:
            self.css = f.read()
        with open("web/script.js") as f:
            self.js = f.read()
    
    def ap(self):
        ap = network.WLAN(network.AP_IF)
        ap.config(ssid="GuessTheGate2", key="LogicIsFun")
        ap.active(True)
        print("IP: ", ap.ifconfig()[0])
    
    def socket(self):
        self.s = socket.socket()
        self.s.bind(("0.0.0.0", 80))
        self.s.listen(1)
        self.s.setblocking(False)
        print("Waiting...")
    
    def serve(self):
        try:
            client, addr = self.s.accept()
            print("Connected from ", addr)
        except OSError:
            return
        
        try:
            request = client.recv(1024).decode()
            print("Request: ", request)
        except OSError:
            return

        if "GET /guess" in request:
            self.main.guess = self.main.options[int(request.split("option=")[1].split(" ")[0])]
            client.send("HTTP/1.1 302 Found\r\n")
            client.send("Location: /\r\n")
            client.send("Connection: close\r\n\r\n")
        else:
            html = self.html \
                .replace("</script>", 
                    "options(" + str(self.main.options) + ");"
                    + "score(" + str(self.main.score) + ");"
                    + "</script>")
            client.send("HTTP/1.1 200 OK\r\n")
            client.send("Content-Type: text/html\r\n")
            client.send("Connection: close\r\n\r\n")
            client.send(html)

        client.close()
