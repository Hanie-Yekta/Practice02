# daryaft maqadir
print("Enter your Weight(kg)")
M = float(input())
print("Enter your height(m)")
H = float(input())
BMI = M / (H * H)
print("BMI:", BMI)

# gozaresh natije
if BMI < 18.5:
    print("Underweight")
elif 18.5 <= BMI <= 24.9:
    print("Normal")
elif 25 <= BMI <= 29.9:
    print("Overweight")
elif 24.9 <= BMI <= 30:
    print("Obese")
elif 35 <= BMI:
    print("Extremely obese")
