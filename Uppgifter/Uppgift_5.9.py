#Är texten palindrom(samma baklänges som framlänges)?
#
a = input('Ange valfri text: ')
a = a.replace(' ', '') #Vi inleder med att ta bort alla blanksteg.
a = a.lower() #Sedan byter vi ut alla versaler till gemener
b = a[::-1] #Med denna funktion vänder vi på texten, genom att använda "-1" läses texten in bakifrån.
if b == a: #Sedan använder vi en vanlig if sats, om "b" är lika med "a" (True) är texten palindrom.
    print(f"Texten är palindrom. Din text = {a} och baklänges = {b}")
else: #Om texten inte är palindrom, skriver vi ut detta.
    print(f'Texten är inte palindrom. Din text = {a} och baklänges = {b}')

