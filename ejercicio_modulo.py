def funcion_suma (numero1, numero2):
	 resultado = int(numero1) + int(numero2)
	 return resultado

def funcion_resta (numero1, numero2):
	 resultado = int(numero1) - int(numero2)
	 return resultado

#suma
print "SUMA"
valor1 = raw_input("escribe un numero: ")
print "+"
valor2 = raw_input("escribe otro numero: ")
print "=" 
resultado = funcion_suma(valor1,valor2)
print resultado

if resultado < 10:
	print "Tu resultado es menor que 10 "
else:
	print "Tu numero es mayor que 10"

if resultado > 100:
	print "Tu resultado es menor que 100"
else:
	print "Pero menor que 100"

#resta
print "RESTA"
valor1 = raw_input("escribe un numero: ")
print "-"
valor2 = raw_input("escribe otro numero: ")
print "+"

variable = funcion_resta(valor1,valor2)
print variable

if variable < 10:
	print "Tu resultado es menor que 10"
else:
	print "Tu numero es mayor que 10"

if resultado > 100:
	print "Tu resultado es menor que 100"
else:
	print "Pero es menor 100"



