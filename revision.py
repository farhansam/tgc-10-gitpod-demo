print("Happy 2021!!!")

weight = float(input("Enter weight in kg:"))
height = float(input("Enter height in metres:"))
bmi = weight / (height * height)
print("Your BMI is:", bmi)

if bmi < 18.5:
    print("Underweight")
elif bmi <= 24.9:
    print("Normal Weight")
elif bmi <= 29.9:
    print("Overweight")
else:
    print("Obese")

