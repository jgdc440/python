"Operaciones de Algebra Modular"

Decenas = 1125 // 20
Residuo = 1125 % 20

print Decenas, Residuo
print Decenas * 20 + Residuo


horalocal = 20
shift = 8
horaFinal = (horalocal + shift) % 24

print "0"+ str(horaFinal)+":00"