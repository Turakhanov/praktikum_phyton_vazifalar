# 28/02/2024
# Author: Data Wizard

#1:
import math
uzunlik = lambda pi, r : 2*pi*r
print(uzunlik(math.pi,10))

#2:
from math import sqrt

sonlar = list(range(11)) 
ildizlar = list(map(sqrt,sonlar))

#3:
kvadratlar = list(map(lambda x:x*x,sonlar))
print(kvadratlar)

#4:
import random as r

sonlar = r.sample(range(100),10) # 0-99 oralig'ida 10 ta tasodifiy sonlar
juft_sonlar = list(filter(lambda son: son%2==0,sonlar))

print(sonlar)
print(juft_sonlar)
