

def escanear(host, puerto):
    print "Escaneando el host: ", host
    print "por el puerto ", puerto
    
ip = str(raw_input("IP:"))
port = int(raw_input("PORT:"))

escanear(ip, port)
