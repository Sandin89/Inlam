#Vill du byta rad i en mening, skriv \n
print("Jag vill att denna text ska stå på två \nrader")

#Om du vill skrive ut ett kvoteringstecken i texten, skriv ett bakvänt snedsträck innan, \" detta låter dig ta med tecknet bakom snedstrecket.'
print("Jag vill att denna text ska stå på två \"rader")

#phrase låter oss skapa en string variabel, underlättar vid en återkommande fras.
phrase = "Code by DS"
print (phrase + " är nice")

#Denna funktion .lower, gör hela texten i små bokstäver. .upper gör den till stora bokstäver.
phrase = "Code by DS"
print (phrase.islower())

#Denna funktion ger oss "true" eller "false", beroende på om texten faktiskt är i stora eller smnå bokstäver.
phrase = "Code by DS"
print (phrase.islower())

#Denna funktion ändrar texten till små bokstäver, sedan kör den funktionen OM texten är i små bokstäver, vilket gör den "true".
phrase = "Code by DS"
print (phrase.lower().islower())

#len räknat ut antalet tecken i texten.
phrase = "Code by DS"
print (len(phrase))

#Denna funktion [0] [1] etc. skriver exempelvis ut den första bokstaven  i stringen.
phrase = "Code by DS"
print (phrase[0])

#index funktion, denna funktion letar upp den angivna bokstaven och skriver ut vilket nummer i ordningen den har. Man kan även söka upp hela ord.
phrase = "Code by DS"
print (phrase.index("D"))
print (phrase.index("Code"))

#Denna funktion byter ut det angivna ordet mot ett nytt.
phrase = "Code by DS"
print (phrase.replace("by", "for"))