class Store:
    name = 'No name Provided'
    location = ' '

class Company(Store):
    storeType = 'Grocery'
    affordability = 'expensive'

class Product(Store):
    foodType = 'healthy'
    productAmount = 5000