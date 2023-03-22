class Prot:
    def __init__(self):
        self.__protectedVar = 0

    def getPriv(self):
        print(self.__privateVar)

    def setPriv(self, private):
        self.privateVar = private
    
num = Prot() #THis places the whole class within an object to be called upon
num._protectedVar = 21 #This changes the variable defined under the function __init__
num.getPriv()
num.setPriv(12)
print(num._protectedVar)
print(num.setPriv)

