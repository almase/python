import os

def version():
     return 1.0

def crea_dir(directorio):
	if os.access(directorio,0):
		print "El directorio ya existe"
	else:
		os.mkdir(directorio)
		print "Directorio "+directorio+" creado"

def entorno():
	for clave,valor in os.environ.iteritems():
		if clave=='USER' or clave=='PATH' or clave=='SHELL':
			print valor


def gordos(directorio,size):
	if size[-1:].upper() not in ('K','M','G'):
		print "Solo K,M,G"
		return false
        tam=int(size[0:-1])
	if size[-1:].upper()=='K':
		bytes=tam*1024
	elif size[-1:].upper()=='M':
		bytes=tam*1024*1024
	else:
		bytes=tam*1024*1024*1024
	
	lista=os.listdir(directorio)
	for fichero in lista:
		if os.path.getsize(directorio+"/"+fichero)> bytes:
			print fichero+" "+ str(os.path.getsize(directorio+"/"+fichero))

def visualizar(fichero):
	if not os.access(fichero,0):
		print 'Fichero no exxiste'
		return False
	f=open(fichero,'r')
	while True:
		linea= f.readline()
		if not linea: break
		print (linea[0:-1])







def visualizar1(fichero):
	if not os.access(fichero,0):
		print 'Fichero no exxiste'
		return False
	f=open(fichero,'r')
	lineas= f.readlines()
	for linea in lineas:
		print (linea[0:-1])





def cp(fichero1,fichero2):
        if not os.access(fichero1,0):
                print "Fichero no existe"
                exit()
        if not os.path.isfile(fichero1):
                print "No es un fichero"
                exit()
        f1=open(fichero1,'r')
        f2=open(fichero2,'w')
        lineas=f1.readlines()
        #f2.writelines(lineas)
        for linea in lineas:
                f2.write(linea)
        f1.close()
        f2.close()

