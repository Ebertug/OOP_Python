class Ucus():                                                           #class oluşturuyoruz
    havayolu = "THY"                                                    #classtaki her objenin ortak özelliği
    
    def __init__(self, kod, kalkis, varis, sure, kapasite, yolcu):      #her objenin sahip olduğu farklı değerdeki özellikler
        self.kod = kod                                                  #self objeye refarans eder kendisine döndürür
        self.kalkis = kalkis
        self.varis = varis
        self.sure = sure
        self.kapasite = kapasite
        self.yolcu = yolcu
        
    def anonsYap(self):                                                 #her obje için ayrı ayrı anons yazmak yerine bunu da self kullanarak yapıyoruz
        print("Havayolu Şirketi: ",self.havayolu,"\n","Uçuş Kodu: ",self.kod,
              "\n","Kalkış Yeri: ",self.kalkis,"\n","Varış Yeri: ",self.varis,
              "\n","Uçuş Süresi(dk): ",self.sure,"\n","Yolcu Kapasitesi: ",self.kapasite,
              "\n","Mevcut Yolcu: ",self.yolcu)

    def koltukSayısı(self): 
        return (self.kapasite - self.yolcu)
        
    def biletSatis(self, biletAdet=1):
        if ((self.yolcu + biletAdet) <= self.kapasite):
            self.yolcu += biletAdet
            print("{} adet bilet satılmıştır, güncel koltuk sayısı {}" .format(biletAdet, self.koltukSayısı()))
        else:
            print("Yetersiz Kapasite")
            
    def biletIptal(self, biletAdet=1):
        if ((self.yolcu - biletAdet) >= 0):
            self.yolcu -= biletAdet
            print("{} adet bilet iptal edilmiştir, güncel koltuk sayısı {}" .format(biletAdet, self.koltukSayısı()))
        else:
            print("Yetersiz yolcu")
            
            
    
    
    
ucus1 = Ucus("TK30","IST","ANK",60,300,300)                             #objenin sahip olduğu özellikleri belirterek obje oluşturuyoruz
ucus2 = Ucus("TK31","IST","IZM",40,300,250)                             #objenin sahip olduğu özellikleri belirterek obje oluşturuyoruz
ucus3 = Ucus("TK32","IST","GZT",90,300,75)                              #objenin sahip olduğu özellikleri belirterek obje oluşturuyoruz

#Ucus.anonsYap(ucus1)                                                   #class içinden fonksiyonu çağırıyoruz ve hangi objeyi kullancağını belirtiyoruz
#ucus2.anonsYap()                                                       #class içinden fonksiyonu çağırıyoruz ve hangi objeyi kullancağını belirtiyoruz

ucus2.biletSatis(5)
ucus2.biletSatis(5)
ucus2.biletSatis(5)

ucus2.biletIptal(5)