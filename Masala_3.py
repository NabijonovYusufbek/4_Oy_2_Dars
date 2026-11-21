class Transport:
  def harakatlanish(self):
    print("Transport harakatlanmoqda.")


class Mashina(Transport):
  def harakatlanish(self):
    print("Mashina yo'lda g'ildiraklar yordamida harakatlanmoqda.")


class Velosiped(Transport):
  def harakatlanish(self):
    print("Velosiped magazinga qarab harakatlanmoqda.")


class Poyezd(Transport):
  def harakatlanish(self):
    print("Poyezd temir yo'lda Toshkentga qarab harakatlanmoqda.")


transportlar = [Mashina(), Velosiped(), Poyezd()]

for t in transportlar:
  t.harakatlanish()