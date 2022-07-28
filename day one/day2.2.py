# 🚨 calculate BMI 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")


new_height = float(height)
new_weight = float(weight)
# print(type(new_height))

bmi = new_weight/new_height**2
print(int(bmi))