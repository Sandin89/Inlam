import math
#Detta program beräknar antalet minuter som användaren tinger för per månad och tar sedan fram ett pris baserat på det.
min = int(input("Hur många minuter ringer du för, per månad: "))
kost = float(input(f"\nDu ringer {min} minuter per månad.\nSkriv nu minutpriset för dina samtal: "))
#När användaren har knappat in "minut" och "kostnad" så gångrar programmet minuter och kostnaden, för att få fram den totala kostnaden per månad.
pris = min * kost
#Om priset överstiger 300:- så gäller if-satsen.
if pris > 300:
    print(f"Du ringer för {pris} kronor i månaden och uppnår därför 10% rabatt.")
    rabatt = pris * 0.10
    nytt_pris = pris - rabatt
#I denna if sats så skrivs den totala kostnaden ut och sedan så räknar programmet ut vad rabbaten på 10% blir, och skriver ut det nya månadspriset.
    print(f"Ditt nya pris blir därför {nytt_pris}")
#Om priset är under 300:- så skrivs enbart månadspriset ut
else:
    print(f"Du ringer för {pris} i månaden.")
