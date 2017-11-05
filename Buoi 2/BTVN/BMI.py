n = float(input("Nhap can nang: "))
cm = float(input("Nhap chieu cao: "))
m = cm/100
BMI = n / (m * m)
if BMI < 16:
    print("Severely underweight")
elif BMI > 16 and BMI < 18.5:
    print("Underweight")
elif BMI > 18.5 and BMI < 25:
    print("Normal")
elif BMI >25 and BMI < 30:
    print("Overweight")
else:
    print("Obese")
