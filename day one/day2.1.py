# type casting = type conversion

# num_char = len(input("what is your name"))

# new_num_char = str(num_char)

# print("your name has "+ new_num_char + "Characters.")

#Code challenge

# 🚨 this code should not change 👇
from __future__ import division
from lib2to3.pgen2.token import PLUS


two_digit_number = input("Type a two digit number: ")
# 🚨 this code should not change 👆

####################################
#this my code 👇
print(type(two_digit_number))
a = (two_digit_number)
c = int(a[0]) + int(a[1])
print(c)


#order of excecuting mathematical operations
# PEMDASLR
# () brackets
# ** exponents
# * multiplication / division (Priority from left )
# 
# + addition 
# - subtraction
