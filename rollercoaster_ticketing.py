print("Welcome to Rollercoaster ticketing.")

height= float(input("What is your height? "))
age= int(input("What is your age? "))

if height >= 100:

    if age <= 7:
        print("Your ticket is $5")
    elif age <= 10:
        print("Your ticket is $7")
    else:
        print("Your ticket is $10")

else:
    print("Sorry, you can't ride")

