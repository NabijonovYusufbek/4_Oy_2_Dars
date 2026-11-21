class Telefon:

  def __init__(self, brend, model, narx):
    self.brend = brend
    self.model = model
    self.narx = narx

  def __str__(self):
    formatlangan_narx = f"{self.narx:,}".replace(",", " ")
    return f"{self.brend} {self.model} — {formatlangan_narx} so'm"

  def __eq__(self, boshqa):
    if isinstance(boshqa, Telefon):
      return self.narx == boshqa.narx
    return False

t1 = Telefon("Samsung", "A54", 4500000)
t2 = Telefon("Redmi", "Note 13", 4500000)
t3 = Telefon("iPhone", "15", 11000000)

print(t1)
print(t2)
print(t3)

print("-" * 40)

print("t1 == t2 (narxi bir xil):", t1 == t2)
print("t1 == t3 (narxi har xil):", t1 == t3)