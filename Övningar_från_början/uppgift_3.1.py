import math

min = int(input("Hur många minuter ringer du för, per månad: "))
kost = float(input(f"\nDu ringer {min} minuter per månad.\nSkriv nu minutpriset för dina samtal: "))
pris = min * kost
if pris > 300:
    print(f"Du ringer för {pris} kronor i månaden och uppnår därför 10% rabatt.")
    rabatt = pris * 0.10
    nytt_pris = pris - rabatt
    print(f"Ditt nya pris blir därför {nytt_pris}")
else:
    print(f"Du ringer för {pris} i månaden.")
