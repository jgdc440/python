a = "1lll1l1l1l1ll1l111ll1l1ll1l1ll1ll111ll1ll1ll1l1ll1ll1ll1ll1lll1l1l1l1l1l1l1l1l1l1l1l1ll1lll1l111ll1l1l1l1l1"

def contar_l(x):
    global contador
    contador = 0
    for letra in x:
        if letra == "l":
            contador = contador + 1
    return(contador)

print contar_l(a)