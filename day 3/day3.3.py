# 🚨 Leap year determinant 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆
if year %4 == 0:
    if year %100 == 0:
        if year %100 == 0:
            print("Leap Year.")
        else:
            print("Not Leap Year.")
    else:
        print("Leap Year.")
else:
    print("Not Leap Year")

#Write your code below this line 👇
