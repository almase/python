import os
x=os.listdir('c:\windows\system32')

for z in x:
   if z[-3:]=='exe':
      print z
	  