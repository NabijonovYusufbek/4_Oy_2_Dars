class Shakl:
  def yuza(self):
    return 0


class Kvadrat(Shakl):
  def __init__(self, tomon):
    self.tomon = tomon

  def yuza(self):
    return self.tomon ** 2


class TogriTortburchak(Shakl):
  def __init__(self, boyi, eni):
    self.boyi = boyi
    self.eni = eni

  def yuza(self):
    return self.boyi * self.eni


shakllar = [Kvadrat(7), TogriTortburchak(3, 7)]

for shakl in shakllar:
  print(f"Shakl yuzasi: {shakl.yuza()}")