#Test project BMI calculator

print("Select Gender : ")
print("1. Male")
print("2. Female")

gender = int(input())

if gender == 1 :
  print("You are male")
elif gender == 2 :
  print("You are Female")
else:
  print("Wrong input")

def calculate_BMI(w, h):
  bmi = w / (h*h)
  bmi = round(bmi,2)

  if bmi < 18.5 :
    print("You are  underweight")
  if bmi >= 18.5 and bmi <= 24.9 :
    print("Your BMI are  normal")
  if bmi >= 25 and bmi <= 29.9 :
    print("You are overweight")
  if bmi >= 30 and bmi <= 40 :
    print("You are  Obese Type 1 (obese)")
  if bmi >= 40.1 and bmi <= 50 :
    print("You are  Obese Type 2 (morbid obese)")
  if bmi >= 50 :
    print("You are  Obese Type 3 (super obese)")
  return bmi

print("Enter you height in m :")
height = float(input())

print("Enter you wieght in Kg :")
weight = float(input())

print("your BMI is: ", calculate_BMI(weight, height))
#bmi = weight/ (height*height)
#print("Your BMI is: ", bmi)
