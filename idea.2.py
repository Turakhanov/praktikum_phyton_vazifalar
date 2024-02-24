# 24/02/2024
# Author: Data Wizard

print("Xush kelibsiz! \n")
def mijoz_data(ism, familiya, tyil, tjoy, email = '', tel = None):
  """Mijozlarning malumotlarini saqlaydi"""
  mijoz = {
    'ism': ism,
    'familiya': familiya,
    'tyil': tyil, 
    'tjoy': tjoy,
    'email': email,
    'tel': tel

  }

  return mijoz

print("Ma'lumotlarni kiriting \n")
mijozlar = []
while True:
  ism = input("Ism: \n")
  familiya = input("Familiya: \n")
  tyil = int(input("Tug'ilgan yil: \n"))
  tjoy = input("Tug'ilgan joy: \n")
  email = input("Email: \n")
  tel = input("Telefon nomer: \n")
  mijozlar.append(mijoz_data(ism, familiya, tyil, tjoy, email, tel))
  javob = input(f"Ma'lumotlar saqlandi!   (yana qo'shasizmi?  yes/no) \n")
  if javob == 'no':
    break

print("Saqlangan ma'lumotlar: \n")


for mijoz in mijozlar:
   if email == '':
     mijoz['email'] = "Nom'alum"
   else: 
     email = mijoz['email']
   print(f"{mijoz['ism'].title()} {mijoz['familiya'].title()} \n" 
         f"{mijoz['tyil']} - yilda {mijoz['tjoy'].title()}da tug'ilgan \n" 
         f"{2024-mijoz['tyil']} yoshda \n" 
         f"email: {mijoz['email']}\n" 
         f"telefon raqami: {mijoz['tel']} \n")

         

end = int(input(f"Sizga dastur yoqdimi?     (0dan 10gacha baholang) \n"))
if end != 10:
  print(f"Javobingiz uchun rahmat! keyingi safar {end} dan oshirishga harakat qilamiz... \n")
else: print("Javobingiz uchun rahmat! \n")
