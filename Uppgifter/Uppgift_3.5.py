längd = int(input("Ange brevets längd: "))
bredd = int(input("Ange brevets bredd: "))
tjocklek = int(input("Ange brevets tjocklek: "))

#
#Här kontrollerar programmet om längden är under 600mm, tjockleken under 100mm och om dessa tre totalt är under 900mm
#Sedan kollar programmet, på raden under, om brevets längd är mindre än 140mm och 90mm tjockleck.
if längd <= 600 and tjocklek <= 100 and längd + bredd + tjocklek <= 900 and \
      längd > 140 and bredd > 90:
    print(f"Brevet kan skickas i vanlig postlåda.")
else:
    print("Brevet kan ej skickas i vanlig postlåda.") 