# 26/02/2024
# Author: Data Wizard

#1:
def katta_harf(matnlar):
  for i in range(len(matnlar)):
    matnlar[i] = matnlar[i].title()


  return matnlar

names = ['alixon', 'valixon']
katta_harf(names[:])
print(names)

#2:
def multiply(*sonlar):
  kopaytma =1
  for son in sonlar:
     kopaytma *= son
  return kopaytma   
    
print(multiply(2,3,4,5))
print(multiply(29,43,483,0))



#3:
def talaba_info(ism, familiya, **malumotlar):
  """Talabalar haqida malumotlar"""
  malumotlar['ism'] = ism
  malumotlar['familiya'] = familiya
  return malumotlar

print(talaba_info('odil', 'ahmedov', yoshi=35, t_joy = 'Toshkent'))
print(talaba_info('akrom', 'zokirov'))

