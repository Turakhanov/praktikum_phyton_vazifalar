# 23/02/2024
# Data Wizard
print(f"Maktabga xush kelibsiz! \n")
parent = {
     'ism': '',
     'familiya': '',
     'f_ismi': '',
     'tel':''
      }
student = {'ism': '',
           'familiya': '',
           't_nomer': '',
           'sinf': ''}
flag = True
while flag:
  ask = input(f"Kimsiz?  (parent/student) \n")
  if ask == 'parent':
     ii = input(f"Ismingizni kiriting: \n")
     parent['ism'] = ii
     ff = input(f"Familiyangizni kiriting: \n")
     parent['familiya'] = ff           
     fi = input(f"Farzandingiz ismi: \n")
     parent['f_ismi'] = fi
     tn = input(f"Telefon nomeringiz: \n")
     parent['tel'] = tn

  else: 
     i = input(f"Ismingizni kiriting: \n")
     student['ism'] = i
     f = input(f"Familiyangizni kiriting: \n")
     student['familiya'] = f           
     t = input(f"Telefon raqamingiz: \n")
     student['tel'] = t
     s = input(f"Nechanchi sinfsiz: \n")
     student['sinf'] = s

  
  k = input(f"Malumotlar saqlandi!   (yana qo'shasizmi yes/no) \n")
  if k == 'no':
     flag = False

