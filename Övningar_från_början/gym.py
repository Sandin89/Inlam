import math
ggr = int(input("Välkommen till Daniels gym, vänligen ange ett ungefärligt antal gånger du tänkt besöka gymmet, per månad: "))
årspris = 2499
styckpris = 29
biljett = ggr * 29
if ggr < 86:
    print(f"Det lönar sig för dig att köpa styck pris då din totala kostnad skulle bli: {biljett}, per år.")
else:
    print(f"Det lönar sig att köpa ett årskort eftersom priset för biljetterna hade landat på: {biljett}.")