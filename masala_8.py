class FilmKutubxonasi:

  def __init__(self, nom, filmlar=None):
    self.nom = nom
    self.filmlar = list(filmlar) if filmlar is not None else []

  def film_qosh(self, film_nomi):
    self.filmlar.append(film_nomi)

  def __len__(self):
    return len(self.filmlar)

  def __getitem__(self, indeks):
    return self.filmlar[indeks]

  def __contains__(self, film_nomi):
    return film_nomi in self.filmlar


kutubxona = FilmKutubxonasi("Milliy Kino Arxivi")
kutubxona.film_qosh("Shum bola")
kutubxona.film_qosh("Mahallada duv-duv gap")
kutubxona.film_qosh("O'tkan kunlar")

print("Filmlar soni:", len(kutubxona))

print("Birinchi film (indeks 0):", kutubxona[0])
print("Oxirgi film (indeks -1):", kutubxona[-1])

print("'Shum bola' bormi?:", "Shum bola" in kutubxona)
print("'Titanik' bormi?:", "Titanik" in kutubxona)