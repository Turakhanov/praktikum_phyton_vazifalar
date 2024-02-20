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


  
