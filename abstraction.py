
#We have to import the abstract method for us to be able to use abstraction
from abc import ABC, abstractmethod

class Rent(ABC):
    def payRent(self, amount):
        print("Your rent this month is: ",amount)

    @abstractmethod
    def payment(self, amount):
        pass

class RentPayment(Rent):

    def payment(self, amount):
        print("You still have a balance of {} for rent this month".format(amount))


money = RentPayment()
money.payRent("$1700")
money.payment("$1700")