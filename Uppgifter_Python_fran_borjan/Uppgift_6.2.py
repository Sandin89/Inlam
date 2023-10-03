s = input('Ange ett valfritt antal heltal: ')
ls = s.split() #s.split skapar en lista i variabeln "ls", där "s.split" skapar element av alla siffror med mellanslag bredvid sig.
talen = [int(t) for t in ls] #Här skapas ytterligare en lista "talen", där vi omvandlar alla element från listan "ls" till heltal "int".
mindre = [t for t in talen if t < 0] #Sedan skapar vi ytterliggare en lista, där vi placerar alla element/tal från listan "talen" och spar endast de element som är mindre än 0.
print('Antalet heltal som är mindre än 0 är:', len(mindre)) #Till sist skriver vi ut alla tal som är mindre än 0, med en length "len", för att skriva ut antalen.
#
