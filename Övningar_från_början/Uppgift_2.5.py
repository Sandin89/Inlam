#Här knappar vi in totala priset
pris = input("Vänligen knappa in priset, ink moms: ")

#Här gör vi om det angivna priset till en "float"
x = float(pris)

#Momsen anger vi som 25%
momsprocent = float(25)

#Sedan tar vi priset som vi angav, gångrar det med momsprocenten och delar sedan det resultatet med 100
moms = (x * momsprocent) / 100

#Här tar jag totala beloppet och drar av momsen, för att ge priset exklusive moms.
exmoms = x - moms

#Vilket ger oss svaret.
print(f"Momsen är {moms}")
print(f"Priset exklusive moms är {exmoms}")
