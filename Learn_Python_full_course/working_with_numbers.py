def print_heltal_mellan_2_och_n(n):
    # Kontrollera om n är ett giltigt heltal mellan 1 och 99
    if not (isinstance(n, int) and 1 <= n <= 99):
        print("N är inte ett giltigt heltal mellan 1 och 99.")
        return
    
    # Skriv ut alla heltal mellan 2 och n
    for i in range(2, n + 1):
        print(i)

def main():
    try:
        n = int(input("Ange ett heltal mellan 1 och 99: "))
        print_heltal_mellan_2_och_n(n)
    except ValueError:
        print("Du måste ange ett heltal.")

if __name__ == "__main__":
    main()
