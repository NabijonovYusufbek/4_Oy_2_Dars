class Mahsulot:

  def __init__(self, nom, narx):
    self.nom = nom
    self.narx = narx

  def __str__(self):
    formatlangan_narx = f"{self.narx:,}".replace(",", " ")
    return f"{self.nom} — {formatlangan_narx} so'm"


class Savat:

  def __init__(self, nom="Xarid savati", mahsulotlar=None):
    self.nom = nom
    self.mahsulotlar = list(mahsulotlar) if mahsulotlar is not None else []

  def qoshish(self, mahsulot):
    self.mahsulotlar.append(mahsulot)

  def __len__(self):
    return len(self.mahsulotlar)

  def __bool__(self):
    return len(self.mahsulotlar) > 0

  def umumiy_narx(self):
    return sum(m.narx for m in self.mahsulotlar)

  def __str__(self):
    return f"{self.nom} ({len(self)} ta mahsulot)"


savat = Savat("Kundalik savat")
savat.qoshish(Mahsulot("Non", 4000))
savat.qoshish(Mahsulot("Sut", 12000))
savat.qoshish(Mahsulot("Olma", 18000))

print(savat)

if savat:
  jami = savat.umumiy_narx()
  formatlangan_jami = f"{jami:,}".replace(",", " ")
  print(f"Savat bo'sh emas. Umumiy narx: {formatlangan_jami} so'm")
else:
  print("Savat bo'sh.")