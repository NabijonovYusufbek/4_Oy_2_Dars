class Inson:
    def __init__(self,ism,yosh):
        self.ism = ism
        self.yosh = yosh


class Talaba(Inson):
    def __init__(self, ism, yosh,universitet,baho):
        super().__init__(ism, yosh)
        self.universitet = universitet
        self.baho = baho

    def natija(self):
        if self.baho < 56:
            return "Qoniqarsiz"
        elif self.baho <= 70:
            return "qoniqarli"
        elif self.baho <= 85:
            return "Yaxshi" 
        elif self.baho <= 100:
            return "A'lo"
        else:
            return "Bunday baho mavjud emas"

t1 = Talaba("Ali",20,"FARDU",86)
print(t1.natija())