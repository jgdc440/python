class Carro():
    
    def __init__(self, marca, color):
        self.marca = marca
        self.color = color
    
    def acelerar(self):
        print "Acelerando el carro de marca " + self.marca + "de color " + self.color
    def frenar(self):
        print "Frenando el carro de marca " + self.marca + "de color " + self.color
        
xmarca = "Ferrari"
xcolor = "Amarillo"
        
Mi_carro = Carro(xmarca, xcolor)
Mi_carro.acelerar()