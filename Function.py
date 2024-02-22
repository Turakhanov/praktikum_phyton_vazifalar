# 22/02/2024
# Author: Data Wizard

#1:
def tg_yil(ism, yosh):
  """Foydalanuvchi ismi va yoshini so'rab, tug'ilgan yilini hisoblovchi funksiya"""
  print(f"{ism.title()} {2024-yosh}-yilda tu'gilgan. \n")

tg_yil('ali', 19)
tg_yil('halil', 24)


#2:
def hisobla(son):
  """Kiritilgan sonning kvadrati va kubini hisoblovchi funksiya"""
  print(f"{son} ning kvadrati = {son**2}, kubi esa = {son**3}")

hisobla(3)
hisobla(4)

#3:
def top(son):
  """Kiritilgan son juftmi yoki toq"""
  if son%2 == 0:
    print(f"{son} - juft son")
  else:
    print(f"{son} - toq son")

top(15)
top(30)

#4:
def solishtir(son1, son2):
  """Kiritilgan sonlarni solishtir"""
  if son1>son2:
    print(f"Eng katta son = {son1}")
  elif son1<son2:
    print(f"Eng katta son = {son2}")
  else: 
    print(f"Kiritilgan sonlar teng!")

solishtir(30,-45)
solishtir(-59,34)
solishtir(0,0)

#5:
def d_kotar(x, y):
  """x ning y - darajasini hisobla"""
  print(x**y)

d_kotar(3,0)
d_kotar(3,1)
d_kotar(3,-1)


#6:
def d_kotar(a, b=2):
  """5-kodda korsatganimdaka"""
  print(a**b)

d_kotar(15)
d_kotar(17)

#7:
def devide(son):
  """Sonni 1dan 10gacha qaysi sonlarga bo'linishini ko'rsat"""
  for a in range(2,11):
    if son%a == 0:
      print(f"{son}, {a} ga qoldiqsiz bo'linadi!")


devide(18)
devide(7)









  







