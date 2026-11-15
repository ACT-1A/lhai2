print("[1] = Snacks")
print("[2] = Drinks")

choi = int(input("Enter your choice:"))
if choi == 1:
    print("Snacks")
    print("[1] = Pyatos  23.00 pesos")
    print("[2] = Noba 25.00 pesos")
    pia = 23
    noba = 25
    choi1 = int(input("Enter your choice of snacks:"))
    if choi1 == 1:
        product = 23.00
        print("Pyatos 23.00")
    elif choi1 == 2:
        product = 25.00
        print("Noba 25.00")
    else:
        print("Invalid Input!")

    quan = int(input("Enter quantity:"))
    subtot = quan * product
    print("Subtotal is:" , subtot)
    csh = int(input("Enter your cash:"))
    tot = csh - subtot
    print("Change is " , tot)

elif choi == 2:
    print("Drinks")
    print("[1] = Coke 20 pesos")
    print("[2] = Royal 25 pesos")
    choi2 = int(input("Enter your choice of drinks:"))
    if choi2 == 1:
        product = 20.00
        print("Coke 20.00")
    elif choi2 == 2:
        product = 25.00
        print("Royal 25.00")


    quantity = int(input("Enter quantity:"))
    subtotal = quantity * product
    print("Subtotal is:" , subtotal)
    cash = int(input("Enter your cash:"))
    total = cash - subtotal
    print("Change is:" , total)

else:
    print("Invalid Input")