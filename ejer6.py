import os
x=os.listdir('c:\windows\system32')
letra=raw_input('Pon una letra:')
ficheros=[]
for z in x:
   if z.count(letra)>0:
		ficheros.append(z)
		print z
print "Total de ficheros:"+str(len(ficheros))
	  