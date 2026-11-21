class Xodim:
    def __init__(self,ism,maosh):
        self.ism = ism
        self.maosh = maosh


class Oqituvchi(Xodim):

    def malumot(self,fan):
        return f"Ism: {self.ism}\nMaoshi: {self.maosh}\nFan: {fan}"


class Farrosh(Xodim):

    def malumot(self,qavat):
        return f"Ism: {self.ism}\nMaosh: {self.maosh}\nQavat: {qavat}"


o1 = Oqituvchi("Zuhra",9000000)
print(o1.malumot("Tarix"))

f1 = Farrosh("Fotima",4000000)
print(f1.malumot(3))