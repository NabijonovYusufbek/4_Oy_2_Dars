class Kitob:
  def __init__(self, nom, muallif, sahifa_soni):
    self.nom = nom
    self.muallif = muallif
    self.sahifa_soni = sahifa_soni

  def malumot(self):
    print(
        f"Kitob: {self.nom} | Muallif: {self.muallif} |"
        f" Sahifalar: {self.sahifa_soni}"
    )


class ElektronKitob(Kitob):
  def __init__(self, nom, muallif, sahifa_soni, format, fayl_hajmi):
    super().__init__(nom, muallif, sahifa_soni)
    self.format = format
    self.fayl_hajmi = fayl_hajmi

  def malumot(self):
    super().malumot()
    print(f"Format: {self.format.upper()} | Hajmi: {self.fayl_hajmi} MB")



o1 = Kitob("O'tkan kunlar", "Abdulla Qodiriy", 320)
e1 = ElektronKitob("Python asoslari", "Alisher Xo'jayev", 240, "pdf", 8.5)

o1.malumot()
print("-" * 55)
e1.malumot()