import os

def version():
     return 1.0

def crea_dir(directorio):
	if os.access(directorio,0):
		print "El directorio ya existe"
	else:
		os.mkdir(directorio)
		print "Directorio "+directorio+" creado"
