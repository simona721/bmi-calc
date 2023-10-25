height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))


bmi = weight/(height*height)
print(f"Your body mass index is: {round(bmi)}")

if(bmi > 0):
    if(bmi <= 16):
        print("You are severely underweight")
    elif(bmi <= 18):
        print("You are underweight")
    elif(bmi <= 25):
        print("You are healthy")
    elif(bmi <= 30):
        print("You are overweight")
    else:
        print("You are severely overweight")



