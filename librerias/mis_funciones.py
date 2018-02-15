def imprimir():
    print 'hola'
	
def funcion():
    return 'hola Mundo'
	
def par_impar(numero):
	if numero%2==0:
		return "par"
	else:
		return "impar"
		
def par_impar1(numero):
   return "par" if(numero%2==0) else "impar"
   

def alta_cliente(dni,nombre,*apellidos):
	print dni
	print nombre
	print "Tienes "+str(len(apellidos))+" apellidos"
	for x in apellidos:
		print x
		
		
def iniciales(nombre,*apellidos):
	ini=nombre[0]+'.'
	for x in apellidos:
		ini=ini+x[0]+'.'
	return ini
	