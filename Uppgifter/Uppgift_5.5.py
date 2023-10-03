# Låt användaren skriva in en text och spara den i variabeln 's'
s = input("Skriv en text: ")
#
# Loopa igenom texten från början till slut med en for-sats
for i in range(0, len(s)):
    # Kolla om det aktuella tecknet (s[i]) är ett mellanslag eller tabbtecken
    if s[i] == " " or s[i] == "\t":
        # Om vi hittar ett vitt tecken, skriv ut dess position och avsluta loopen
        print(f"Första vita tecken finns på plats nr {i:d}")
        break
else:
    # Om ingen loop avbryts (dvs. inga vita tecken hittades), skriv ut att det inte finns några
    print("Inga vita tecken")
