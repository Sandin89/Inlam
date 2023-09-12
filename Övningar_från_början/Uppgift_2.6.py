#Här knappar vi in den totala tiden i sekunder
tid = int(input("Vänligen ange ett valfritt antal sekunder: "))
#Här omvandlar vi sekunderna till hela timmar
tim = tid // 3600
#Resterande sekunder tar vi och omvandlar till minutrar
rest = tid % 3600
min = rest // 60
#Till sist tar vi resterande sekundrar från minutrarna och omvandlar dem till sekunder
sek = rest % 60
#Programmet skriver nu ut denm totala tiden
print(f"{tid} = {tim} timmar, {min} minuter och {sek} sekunder")