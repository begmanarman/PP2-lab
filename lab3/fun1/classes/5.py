

class Bank:
    def __init__(self,name,many):
        self.name=name
        self.many=many
    def owner(self):
        return self.name

    def balance(self):
        return self.many
    
    def deposit(self,many):
        self.many+=many
        return self.many
    
    def  withdraw(self,many):
        if self.many - many < 0:
            return "insufficient funds"
        else:
           self.many -= many
           return self.many 
        

name = input("Owner :")
many = float(input("balance:"))
x = Bank(name,many)


print(x.owner())
print(x.balance())
sum= float(input("deposit:"))
print(x.deposit(sum))
minus =float(input("withdraw:"))
print(x.withdraw(minus))

