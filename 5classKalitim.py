class Seyehat():
    
    def __init__(self, kalkis, varis):
        self.kalkis = kalkis
        self.varis = varis
        
    def anons(self):
        print("{}-{} seferi".format(self.kalkis, self.varis))
        

class Otobus(Seyehat):
    def __init__(self, aracBoy, kalkis, varis):
        Seyehat.__init__(self, kalkis, varis)
        self.aracBoy = aracBoy
        

oto1= Otobus("3","GZT","ANK")

oto1.anons()
print(oto1.aracBoy)