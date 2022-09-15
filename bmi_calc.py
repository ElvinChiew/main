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

print("Enter you height in m :")
height = float(input())

print("Enter you wieght in Kg :")
weight = float(input())

bmi = weight/ (height*height)
print("Your BMI is: ", bmi)
