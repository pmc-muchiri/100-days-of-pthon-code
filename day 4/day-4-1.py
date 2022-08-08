#randomization of number
# import random 
# randomInteger = random.randomint(1, 10)
# print(randomInteger)

# randomFloat = random.random() *5
# print(randomFloat)
#Write your code below this line 👇
#Hint: Remember to import the random module first. 🎲
import random

randomFaces = random.randint(0,1)
if randomFaces == 1:
  print("Head")
else:
  print("Tail")
  

