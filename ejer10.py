import librerias.ficheros
import sys



if len(sys.argv) <> 2:
	print "Error, necesito el directorio"
else:
	librerias.ficheros.crea_dir(sys.argv[1])
