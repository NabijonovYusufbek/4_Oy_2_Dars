class Karta:

  def __init__(self, egasi, raqam_oxiri, balans):
    self.egasi = egasi
    self.raqam_oxiri = str(raqam_oxiri)
    self.balans = balans

  def __str__(self):
    formatlangan_balans = f"{self.balans:,}".replace(",", " ")
    return (
        f"Karta egasi: {self.egasi} (**{self.raqam_oxiri}) | Balans:"
        f" {formatlangan_balans} so'm"
    )

  def __gt__(self, boshqa):
    if isinstance(boshqa, Karta):
      return self.balans > boshqa.balans
    return NotImplemented

  def __lt__(self, boshqa):
    if isinstance(boshqa, Karta):
      return self.balans < boshqa.balans
    return NotImplemented

karta1 = Karta("Azizbek Karimov", "4821", 3200000)
karta2 = Karta("Madina Rasulova", "9014", 5750000)

print(karta1)
print(karta2)
print("-" * 55)

if karta1 > karta2:
  print(f"Mablag' ko'proq: {karta1.egasi} kartasida.")
elif karta1 < karta2:
  print(f"Mablag' ko'proq: {karta2.egasi} kartasida.")
else:
  print("Ikkala kartada ham mablag' teng.")