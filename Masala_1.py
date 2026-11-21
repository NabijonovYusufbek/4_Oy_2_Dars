class Hayvon:
    def __init__(self,nomi,yosh):
        self.nomi = nomi
        self.yosh = yosh

    def ovoz(self,ovoz1):
        return f"{self.nomi}: {ovoz1} deb ovoz chiqaradi"


class It(Hayvon):
    def qoriqlash(self):
        return f"{self.nomi} uyni qo'riqladi"

    def ovoz(self, ovoz1):
        return super().ovoz(ovoz1)


class Mushuk(Hayvon):
    def sichqon_tutish(self):
        return f"{self.nomi} uyda sichqon tutdi"

    def ovoz(self, ovoz1):
        return super().ovoz(ovoz1)

i1 = It("Olopar",3)
m1 = Mushuk("Mosh",2)

print(i1.qoriqlash())
print(i1.ovoz("vooooov!"))

print(m1.sichqon_tutish())
print(m1.ovoz("myooo!"))

