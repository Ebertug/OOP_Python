class Ucus():               #class oluşturuyoruz
    havayolu = "THY"        #Her objenin sabit özelliği
                            
    def __init__(self,kod): #her objede bulunması gereken farklı değerlerdeki özellikler
        self.kod = kod

ucus1 = Ucus("TK32")        #class'a ait bir obje oluşturuyoruz
ucus2 = Ucus("TK29")         
print(ucus1.havayolu)       #objenin havayolu özelliğini ekrana yazdırıyoruz
print(ucus1.kod) 
print()           
print(ucus2.havayolu)
print(ucus2.kod)     