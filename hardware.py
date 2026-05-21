from machine import Pin

class Hardware:
    def __init__(self):
        self.input_a = Pin(0, Pin.IN)
        self.input_b = Pin(1, Pin.IN)
        self.led = Pin(2, Pin.OUT)
        
        self.power = Pin(15, Pin.OUT)
        self.power.value(True)
    
    def inputs(self):
        return self.input_a.value(), self.input_b.value()

    def logic(self, gate, a, b):
        if gate == "AND":
            result = a and b
        elif gate == "OR":
            result = a or b
        elif gate == "NAND":
            result = not(a and b)
        elif gate == "NOR":
            result = not(a or b)
        elif gate == "XOR":
            result = a ^ b
        elif gate == "XNOR":
            result = not(a ^ b)
        else:
            result = False

        return result
    
    def output(self, gate):
        a, b = self.inputs()
        result = self.logic(gate, a, b)
        self.led.value(result)
