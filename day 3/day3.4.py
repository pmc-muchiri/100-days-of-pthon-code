# if do
# 🚨 Pizza Delivery 👇
pizza_bill = 0
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L :")
add_pepperoni = input("Do you want pepperoni? Y or N : ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
# 🚨 Don't change the code above 👆

if size == "S":
    pizza_bill += 15
elif size == "M":
    pizza_bill += 20
else:
    pizza_bill += 25

if add_pepperoni == "Y":
    if size == "S":
        pizza_bill = +2
    else:
        pizza_bill = +3

if extra_cheese == "Y":
    pizza_bill = +1

 
print(f"your final bill is:${pizza_bill} ")
    

#Write your code below this line 👇
