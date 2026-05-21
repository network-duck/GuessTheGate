import random
from hardware import Hardware
from server import Server

class Main:
    def __init__(self):
        self.gates = ["AND", "OR", "NAND", "NOR", "XOR", "XNOR"]
        self.gate = None
        self.options = []
        self.guess = None
        self.score = -1
        
        self.hw = Hardware()
        self.server = Server(self)

    def round(self):
        if self.gate == self.guess:
            self.score += 1
        
        self.gate = self.gates[random.randint(0, len(self.gates) - 1)]
        self.optioner()
        self.guess = None

    def optioner(self):
        self.options = []

        while len(self.options) < 4:
            g = self.gates[random.randint(0, len(self.gates) - 1)]
            if g not in self.options:
                self.options.append(g)
        
        if self.gate not in self.options:
            self.options[random.randint(0, 3)] = self.gate

        return self.options
    
    def game(self):
        self.round()
        while True:
            if self.guess is not None:
                self.round()

            self.hw.output(self.gate)
            self.server.serve()

def __main__():
    main = Main()
    main.game()

if __name__ == "__main__":
    __main__()