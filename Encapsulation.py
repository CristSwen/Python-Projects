class Prot:
    def __init__(self):
        self.__protectedVar = 0

    def getPriv(self):
        print(self.__privateVar)

    def setPriv(self, private):
        self.privateVar = private
    
num = Prot()
num._protectedVar = 21
num.getPriv()
num.setPriv(12)
print(num._protectedVar)
print(num.setPriv)

