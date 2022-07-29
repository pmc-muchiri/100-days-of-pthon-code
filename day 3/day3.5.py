# logical operators
# Lovcalce 
# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


combine_names = name1 + name2
lowerCaseName = combine_names.lower()

t = lowerCaseName.count("t")
r = lowerCaseName.count("r")
u = lowerCaseName.count("u")
e = lowerCaseName.count("e")
true = t + r + u + e

l = lowerCaseName.count("l")
o = lowerCaseName.count("o")
v = lowerCaseName.count("v")
e = lowerCaseName.count("e")

love = l + o + v + e

lovecomb = str(true) + str(love)
lovePercentage = int(lovecomb)


if lovePercentage <10 or lovePercentage >90:
    print(f"Your love score is {lovePercentage} you are going forever")
elif lovePercentage >=40 or lovePercentage<=50:
    print(f"Your score is {lovePercentage} You're alright together mate.")
else:
    print(f"Your love score is {lovePercentage}")