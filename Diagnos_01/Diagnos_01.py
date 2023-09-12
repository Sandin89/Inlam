# Funktion för att kontrollera om ett tal är ett primtal
def is_prime(number):
# Om talet är mindre än eller lika med 1, är det inte ett primtal
    if number <= 1:  
        return False
# Om talet är 2 eller 3, är det ett primtal
    if number <= 3:  
        return True
# Om talet är jämnt delbart med 2 (utom 2 och 3), är det inte ett primtal
    if number % 2 == 0:  
        return False
    i = 5
# Loopa så länge i * i är mindre än eller lika med talet
    while i * i <= number:  
# Om talet är delbart med i, är det inte ett primtal
        if number % i == 0:  
            return False
# Hoppa över jämna tal genom att öka i med 2 varje gång
        i += 2  
# Om inget av ovanstående villkor uppfylls, är talet ett primtal
    return True  

# Funktion för att hitta alla primtal upp till ett visst tal (limit)
def find_primes(limit):
# Skapa en tom lista för primtalen
    prime_list = []  
# Loopa från 2 till limit
    for i in range(2, limit + 1):  
# Om i är ett primtal enligt is_prime-funktionen, lägg till det i listan
        if is_prime(i):  
            prime_list.append(i)
# Returnera listan med primtalen
    return prime_list  

# Läs in ett heltal från användaren som fungerar som övre gränsen (limit)
limit = int(input("Vänligen ange ett heltal mellan 1 och 99: "))
# Använd funktionen för att hitta primtalen upp till limit

# Kontrollera om limit är större än 99, om så är fallet, sätt limit till 99
if limit > 99:
    limit = 99
primes = find_primes(limit)  
print("Primtalen upp till", limit, "är:", primes)  

"""Denna kod kan jag ej ta åt mig hela äran för, majoriteten har jag skrivit själv men jag fick använda mig at forum och youtube för att få ihop koden där min kunskap inte räckte till. 
Då jag var hemma med sjukt barn förra fredagen så var jag inte på plats när diagnos 1 gicks igenom, därför sökte jag efter lösningar där jag inte kunde slutföra koden, innan jag senare fick höra av klasskamrater att uppgiften inte behöve vara 100%
Jag kan söka och hitta lösningar till avancecrade koder men vill vara extra tydlig med att jag inte skrivit allt detta själv och målet är att utbilda mig djupare så att jag ej behöver söka efter lösningar på enklare uppgifter."""