print("Wecome to BMI Calculator")
weight = int(input("What is your weight? "))
height = float(input("What is yoyr height? "))
bmi = weight /(height ** 2)

if bmi <= 18:
    print("You are Skinny")

elif bmi <= 25:
    print("You are Healthy")

else:
    print("You are too Fatty")







