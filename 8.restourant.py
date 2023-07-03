class Restourants:
    
    def __init__(self,name,menu,):
        self.name = name
        self.menu = menu
    
    def displayMenu(self):
        print(f"{self.name}'in menusu {self.menu}")
    
    def addMenu(self,item):
        self.menu.append(item)
    
    def deleteMenu(self):
        pass


rest1 = Restourants("Rest1",["Baklava","Kadayif","Sutlac"])
rest2 = Restourants("Rest2",["Latte","Americano","Berry"])
rest3 = Restourants("Rest3",["Iskender","Adana","Lahmacun"])

rests = [rest1,rest2,rest3]

rest1.addMenu("Deneme")

i = 0 
while i < len(rests):
    # try:
    #     rests[i].displayMenu()
    #     i +=1
    # except IndexError:
    #     print("Başka restourant yok")
    rests[i].displayMenu()
    i +=1