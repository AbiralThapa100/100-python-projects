print("Welcome to Rollercoaster ticketing.")

height= int(input("What is your height in cm? "))
age= int(input("What is your age? "))
bill = 0
if height >= 100:

    if age <= 7:
        bill = 5
        print("Your ticket is $5")
    elif age <= 20:
        bill = 7
        print("Your ticket is $7")
    else:
        bill = 10
        print("Your ticket is $10")

    want_photo = input("Do you want a photo taken? Y or N.")
    if want_photo == "Y":
        bill += 3

    print(f"Your final bill is {bill}")

else:
    print("Sorry, you can't ride")

