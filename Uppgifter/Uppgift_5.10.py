# Skriv ut dagens datum och tid.
#
import datetime #Vi importerar modulen för tid och datum

a = datetime.datetime.now() #Vi skapar variabeln som innehåller datum och tiden.
b = a.date() #Vi skapar ytterliggare en variabel med enbart datumen
c = a.time() #Samt en variabel som innehåller tiden
d = str(c)[:8] #Vi omvandlar variabeln till en "str" och tar bort mikrosekunder genom att ange upp till [:8]
print(f'Dagens datum: {b} \nKlockan är: {d}')