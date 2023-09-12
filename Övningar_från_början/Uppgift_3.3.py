#Jag valde att ta med "import math" för att få in det som vana, även om det nödvändigtvis inte behövs för detta program.
import math
#Programmet inleds med att användaren får skriva in sin poäng från det påhittade provet.
betyg = int(input("Vänligen ange vilken poäng du fick på provet(0-50): "))
#if-satsen jämför om den angivna poängen är värt betyget "A", alltså om poängen är lika med eller över 45 till 50 poäng.
if 45 <= betyg < 50:
    print("Grattis, du fick betyget \"A\"")
#Nedan kommer resterande elif-satser, där betygen "B" till "E" jämförs.
elif 40 <= betyg < 45:
    print("Grattis, ditt betyg blev \"B\"")
elif 35 <= betyg < 40:
    print("Grattis, ditt betyg blev \"C\"")
elif 30 <= betyg < 35:
    print("Grattis, ditt betyg blev \"D\"")
elif 25 <= betyg < 30:
    print("Grattis, ditt betyg blev \"E\"")
elif 25 <= betyg < 0:
    print("Tyvärr, ditt betyg blev \"F\" ")
#Om något tal utanför 0-50 anges, så ges en felkod.
else:
    print("Tyvärr, det angivna betyget stämmer inte.")