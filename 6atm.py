#BURADA BİR ATM SIM OLACAK
i = 0
class ATM():
    
    def __init__(self,name,lastname,balance,accNo):
        self.name = name
        self.lastname = lastname
        self.balance = balance
        self.accNo = accNo
        
    def display(self):
        print("*"*25)
        print("Name: {}\nLastname: {}\nAccount No: {}\nBalanec: {}".format(self.name,self.lastname,self.accNo,self.balance))
        print("*"*25)
        
    def addBalance(self,money):
        self.balance += money

user1 = ATM("Ali", "Yilmaz", 1252,513)
user2 = ATM("Mehmet", "Yilmaz", 4563,624)
user3 = ATM("Hasan", "Yilmaz", 2561,735)

users = [user1,user2,user3]

user1.addBalance(4125)
user1.addBalance(-1523)


while (i != len(users)):
    
        users[i].display()
        i +=1
