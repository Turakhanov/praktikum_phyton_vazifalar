# 27/02/2024
# Author: Data Wizard


#1:
import math

x=400
print(math.sqrt(x))

#2:
import random as r 

son = r.randint(0,100) 
print(son)


#3:
ismlar = ['olim','anvar','hasan','husan']
ism = r.choice(ismlar) 
print(ism)
print(r.choice(ism)) 


#4:
x = list(range(0,51,5))
print(x)
print(r.choice(x))


#5:
x = list(range(11))
print(x)
r.shuffle(x)
print(x)
