# 03/03/2024
# Author: Data Wizard

#1:
class = Avto:
  def __init__(self, model, rang, narh):
    """Avtolarning xusisiyatlari"""
    self.model = model
    self.rang = rang
    self.karobka = 'avtomat'
    self.narh = narh

  def get_info(self):
    return f"{self.rang.title()} {self.model.title()}, karobka - {self.karobka.title()}, narhi - {self.narh} \n"


avto1 = Avto('malibu', 'qora', 30000)
print(avto1.get_info())


#2:
class Avto:
  def __init__(self, model, rang, narh):
    """Avtolarning xusisiyatlari"""
    self.model = model
    self.rang = rang
    self.karobka = 'avtomat'
    self.narh = narh
    self.km = 0

  def get_info(self):
    return f"{self.rang.title()} {self.model.title()}, karobka - {self.karobka.title()}, {self.km} km yurgan, narhi - {self.narh} \n"

  def set_km(self, km):
    """Km yangilaydi"""
    self.km = km

  def update_km(self):
    """Km ko'paytiradi"""
    self.km += 1000


avto1 = Avto('malibu','qora', 30000)
print(avto1.get_info())
avto1.update_km()
print(avto1.get_info())
avto1.update_km()
print(avto1.get_info())




































