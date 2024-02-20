# 20/02/2024
# Amaliyot
# Author: Data Wizard

print("Sizning kutubxonangiz")
a = "Yaxshi ko'rgan kitobingiz nomini kiriting: \n"
a += "(dasturni to'xtatish uchun 'exit' deb yozing) \n"
b = ''
s = 0
while True:
  if b != 'exit':
    b = input(a)
    s += 1
  else: break
print("Dastur to'xtadi")

print(f"Kutubxonaga yangi kitoblar qo'shamiz, kitoblar soni: {s}.\n")


# 2:

print("Muzeyga xush kelibsiz!!!")
savol = "Yoshingizni kiriting: \n"
while True:
  j = input(savol)
  if j == 'exit' or j== 'quit':
    break
  yosh = int(j)
  if yosh <= 7:
    narh = 2000
  elif 7 < yosh <= 18:
    narh = 3000
  elif 18 < yosh <=65:
    narh = 10000
  else:
    narh = 0

  if narh == 0:
      print("Sizga chipta bepul")
  else: 
      print(f"Chipta {narh} so'm")  
    


    














  
