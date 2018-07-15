# -*- coding: 850 -*-
# -*- coding: utf-88 -*-

class Electrodomestico:
    
    def __init__(self, tipo):
        
        self.tipo = tipo
        self.encendido = False
        
    def encender(self):
        if self.encendido == False:
            print "Ha sido encendido el " + self.tipo
        else :
            self.encendido = True
            print "El " + self.tipo + " ya estaba encendido"
            
    def apagar(self):
        if self.encendido == False:
            print "Ha sido apagado el " + self.tipo
        else :
            self.encendido = True
            print "El " + self.tipo + " ya estaba apagado"
            
class Celular(Electrodomestico):
    
    def enviarSMS(self):
        print "Enviando SMS"
        
    def llamarVoz(self):
        print "Llamando"
        
class Televisor(Electrodomestico):
    
    def cambiarCh(self):
        print "Cambiando canales"


celular = Celular("iPhone")
televisor = Televisor("Samsung")
celular.encender()
celular.enviarSMS()
celular.llamarVoz()
celular.apagar()
televisor.encender()
televisor.cambiarCh()

raw_input()



            
            
        
        