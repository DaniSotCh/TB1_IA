from Models.Product import Product
from Models.NutritionalInformation import NutInformation

class ProductService:
    def __init__(self):
        super().__init__()
    
    def getProducts(self):
        self.prodList = []
        self.prodList.append(Product('Lentejas', 15, 5, [NutInformation('Grasa', 0.02),\
            NutInformation('Carbs', 0.1), NutInformation('Azucar', 0.15)]))
        self.prodList.append(Product('Atun', 3.5, 0.6, [NutInformation('Grasa', 0.2),\
            NutInformation('Carbs', 0.02), NutInformation('Azucar', 0.05)]))
        return self.prodList