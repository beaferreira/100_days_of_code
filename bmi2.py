weight = float(input())
height = float(input())

bmi = round(weight / height ** 2)

if bmi < 18.5:
    print(f"Your bmi is {bmi}, you are underwight")
elif bmi < 25:
        print(f"Your bmi is {bmi}, you have a normal weight")
elif bmi < 30:
        print(f"Your bmi is {bmi}, you are slightly overweight")
elif bmi < 35:
        print(f"Your bmi is {bmi}, you are obese")
else:
    print("You are clinically obese.")