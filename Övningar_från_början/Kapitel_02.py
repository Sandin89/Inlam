def menu():
    print("[1] Kapitel 2")
    print("[2] Kapitel 3")
    print("[3] Kapitel 4")
    print("[4] Kapitel 5")
    print("[5] Kapitel 6")

menu()
option = int(input("Välj vilket kapitel du önskar titta närmare på: "))

while option != 0:
    if option == 1:
        print("Kapitel 2")

        #Intro
        namn = input("Vad heter du? ")
        print ("Hej,", namn)
        
    elif option == 2:
        print("Kapitel 3")
    elif option == 3:
        print("Kapitel 4")
    elif option == 4:
        print("Kapitel 5")
    elif option == 5:
        print("Kapitel 6")
    else:
        print("Ej möjligt alternativ")

    print()
    menu()
    option = int(input("Välj ett annat kapitel du önskar titta närmare på: "))

print("Tack för besöket.")


#Intro
namn = input("Vad heter du? ")
print ("Hej,", namn)

text1 = ("humle")
text2 = ("dumle")
print (text1, text2)

#Uppgift 2.1, tilldela värden till variablerna "a, b och c."
a = 12
b, c = 12.0, "12.0"

#Variabeln a är en "int"
print(f"Variabeln a har värdet {a}")
#Variabeln b är av typen "float" och variabeln c är av typen "str" eftersom fnuttarna är runt värdet "12.0" 
print(f"Variablerna b och c har värdena {b} och {c}")

