from Models.Product import Product
from random import randint
import math

class ProductService:
    def __init__(self):
        super().__init__()
        self.prodList = []
        self.prodList.append(Product('Lentejas', 2.80, 4, 351, 1.80, 54.0, 23.8))
        self.prodList.append(Product('Atun', 4.50, 4, 102, 2.40, 0.00, 18.9))
        self.prodList.append(Product('Tallarines', 2.20, 2, 301, 2.40, 57.3, 11.8))
        self.prodList.append(Product('Leche', 3.50, 4, 149, 7.90, 11.7, 7.70))
        self.prodList.append(Product('Arroz', 5.33, 3, 205, 0.40, 44.5, 4.30))
        self.prodList.append(Product('Avena', 2.00, 5, 607, 10.8, 103.4, 26.3))
        self.prodList.append(Product('Aceite', 7.50, 2, 120, 13.6, 0.00, 0.00))
        self.prodList.append(Product('Azucar', 3.50, 3, 16.0, 0.00, 4.10, 0.08))
        self.prodList.append(Product('Frijoles', 7.00, 4, 44.0, 0.40, 9.90, 2.40))
        self.prodList.append(Product('Salsa roja', 2.30, 2, 176, 1.10, 35.8, 5.60))
        self.prodList.append(Product('Mantequilla', 7.50, 2, 102, 11.5, 0.10, 0.10))
        self.prodList.append(Product('Sobre de pure de papa', 3.80, 3, 237, 8.90, 35.3,3.90))
        self.prodList.append(Product('Harina', 3.90, 4, 349, 2.26, 69.1, 10.4))
        self.prodList.append(Product('Aceitunas', 15.0, 2, 10.0, 0.90, 0.50, 0.08))
        self.prodList.append(Product('Yogurt', 6.20, 4, 149, 8.00, 11.4, 8.50))
    #Name   Price(sol)   Weight(1-5)  Calories(kcal)	Fat(g)	Carbs (g)	Protein (g)
    def getProducts(self):
        
        return self.prodList

    def addRandomProducts(self, cost, basket):
        tempBasket = basket
        cont = self.priceCalc(tempBasket)
        tempNewBaket = basket
        while(cont<=cost):
            tempBasket.append(self.prodList[randint(0,len(self.prodList)-1)])
            cont = self.priceCalc(tempBasket)
            if(cont<=cost):
                tempNewBaket=tempBasket
        return tempNewBaket

    def randomProduct(self):
        return self.prodList[randint(0,len(self.prodList)-1)]

    def priceCalc(self, basket):
        sum = 0
        for i in basket:
            sum += i.price
        return sum
    
    def caloriesCalc(self, basket):
        sum = 0
        for i in basket:
            sum += i.calories
        return sum
    
    def weightCalc(self, basket):
        sum = 0
        for i in basket:
            sum += i.weight
        return sum
    
    def fatCalc(self, basket):
        sum = 0
        for i in basket:
            sum += i.fat
        return sum
        
    def carbsCalc(self, basket):
        sum = 0
        for i in basket:
            sum += i.carbs
        return sum
    
    def proteinCalc(self, basket):
        sum = 0
        for i in basket:
            sum += i.protein
        return sum

    def simulatedAnnealingNormal(self, temp, basket, cost):
        actualBasket = basket
        betterBasket = basket
        newBasket = basket

        while(temp>1):
            productA = self.randomProduct()
            productB = self.randomProduct()

            iNewBasket1 = randint(0, len(newBasket)-1)
            iNewBasket2 = randint(0, len(newBasket)-1)
            tempBasket=newBasket
            while(self.priceCalc(newBasket)<=cost):
                while(iNewBasket1==iNewBasket2):
                    iNewBasket2 = randint(0, len(newBasket)-1)
                newBasket[iNewBasket1] = productA
                newBasket[iNewBasket2] = productB
                if(self.priceCalc(newBasket)<=tempBasket):
                    tempBasket=newBasket
            newBasket=tempBasket

            newBasket= self.addRandomProducts(cost, newBasket)

            eProteinsActual = self.priceCalc(actualBasket)
            eProteinsNew = self.priceCalc(newBasket)
            eCaloriesActual = self.caloriesCalc(actualBasket)
            eCaloriesNew = self.caloriesCalc(newBasket)
            eWeightActual = self.weightCalc(actualBasket)
            eWeightNew = self.weightCalc(newBasket)
            probP = 0
            probC = 0
            probW = 0
            propMedia = 0

            if(eProteinsNew > eProteinsActual and eCaloriesNew > eCaloriesActual and eWeightNew > eWeightActual):
                propMedia = 1
            else:
                probP = math.exp(( eProteinsNew - eProteinsActual)/temp)
                probC = math.exp(( eCaloriesNew - eCaloriesActual)/temp)
                probW = math.exp(( eWeightNew - eWeightActual)/temp)
                propMedia = ( probP + probC + probW )/3
            
            if(propMedia > (randint(0,100)/10000)):
                actualBasket = newBasket

            if(eProteinsNew > eProteinsActual and eCaloriesNew > eCaloriesActual and eWeightNew > eWeightActual):
                betterBasket = actualBasket

            temp = (1-(0.003))*temp
        return betterBasket
    
    def simulatedAnnealingFat(self, temp, basket, cost):
        #-fat -calories +weight
        actualBasket = basket
        betterBasket = basket
        newBasket = basket
        while(temp>1):
            productA = self.randomProduct()
            productB = self.randomProduct()
            iNewBasket1 = randint(0, len(newBasket)-1)
            iNewBasket2 = randint(0, len(newBasket)-1)
            tempBasket=[]
            while(self.priceCalc(newBasket)<=cost):
                while(iNewBasket1==iNewBasket2):
                    iNewBasket2 = randint(0, len(newBasket)-1)
                newBasket[iNewBasket1] = productA
                newBasket[iNewBasket2] = productB
                if(self.priceCalc(newBasket)<=tempBasket):
                    tempBasket=newBasket
            newBasket=tempBasket
            newBasket= self.addRandomProducts(cost, newBasket)

            eFatActual = self.fatCalc(actualBasket)
            eFatNew = self.fatCalc(newBasket)
            eCaloriesActual = self.caloriesCalc(actualBasket)
            eCaloriesNew = self.caloriesCalc(newBasket)
            eWeightActual = self.weightCalc(actualBasket)
            eWeightNew = self.weightCalc(newBasket)
            probP = 0
            probC = 0
            probW = 0
            propMedia = 0
            if(eFatNew < eFatActual and eCaloriesNew < eCaloriesActual and eWeightNew > eWeightActual):
                propMedia = 1
            else:
                probP = math.exp((eFatActual - eFatNew)/temp)
                probC = math.exp((eCaloriesActual - eCaloriesNew)/temp)
                probW = math.exp((eWeightNew - eWeightActual)/temp)
                propMedia = ( probP + probC + probW )/3

            if(propMedia > (randint(0,100)/10000)):
                actualBasket = newBasket
            if(eFatNew < eFatActual and eCaloriesNew < eCaloriesActual and eWeightNew > eWeightActual):
                betterBasket = actualBasket
            temp = (1-(0.003))*temp
        return betterBasket

    def simulatedAnnealingAnemic(self, temp, basket, cost):
        actualBasket = basket
        betterBasket = basket
        newBasket = basket
        while(temp>1):
            productA = self.randomProduct()
            productB = self.randomProduct()
            iNewBasket1 = randint(0, len(newBasket)-1)
            iNewBasket2 = randint(0, len(newBasket)-1)
            tempBasket=[]
            while(self.priceCalc(newBasket)<=cost):
                while(iNewBasket1==iNewBasket2):
                    iNewBasket2 = randint(0, len(newBasket)-1)
                newBasket[iNewBasket1] = productA
                newBasket[iNewBasket2] = productB
                if(self.priceCalc(newBasket)<=tempBasket):
                    tempBasket=newBasket
            newBasket=tempBasket
            newBasket= self.addRandomProducts(cost, newBasket)

            #+proteins +carbs +weight
            eProteinsActual = self.priceCalc(actualBasket)
            eProteinsNew = self.priceCalc(newBasket)
            eCarbsActual = self.carbsCalc(actualBasket)
            eCabsNew = self.carbsCalc(newBasket)
            eWeightActual = self.weightCalc(actualBasket)
            eWeightNew = self.weightCalc(newBasket)
            probP = 0
            probC = 0
            probW = 0
            propMedia = 0
            if(eProteinsNew > eProteinsActual and eCabsNew > eCarbsActual and eWeightNew > eWeightActual):
                propMedia = 1
            else:
                probP = math.exp((eProteinsNew - eProteinsActual)/temp)
                probC = math.exp((eCabsNew - eCarbsActual)/temp)
                probW = math.exp((eWeightNew - eWeightActual)/temp)
                propMedia = ( probP + probC + probW )/3

            if(propMedia > (randint(0,100)/10000)):
                actualBasket = newBasket
            if(eProteinsNew > eProteinsActual and eCabsNew > eCarbsActual and eWeightNew > eWeightActual):
                betterBasket = actualBasket
            temp = (1-(0.003))*temp
        return betterBasket
            
    def postSimulatedAnnealing(self, cost, familyType):
        temp = 10000
        basket = []
        basket = self.addRandomProducts(cost, basket)
        print("----cost------ ",cost)
        print("----aia------ ",self.priceCalc(basket))
        betterBasket = []

        #Normal : +proteins +calories +weight
        if(familyType=="normal"):
            betterBasket = self.simulatedAnnealingNormal(temp,basket, cost)

        #Fat : -fat -calories +weight
        elif(familyType=="fat"):
            betterBasket = self.simulatedAnnealingFat(temp,basket, cost)

        #Anemic : +proteins +carbs +weight
        elif(familyType=="anemic"):
            betterBasket = self.simulatedAnnealingAnemic(temp,basket, cost)
        
        totalCost = self.priceCalc(betterBasket)
        totalCount = len(betterBasket)
        listBetterBasket =[]
        for i in betterBasket:
            listBetterBasket.append({
                'Name': i.name,
                'Price(s/.)': i.price,
                'Weight(1-5)': i.weight,
                'Calories(kcal)': i.calories,
                'Fat(g)': i.fat,
                'Carbs(g)': i.carbs,
                'Protein(g)': i.protein
            })
        result = {
            'totalCost': totalCost,
            'totalCount': totalCount,
            'betterBasket' : listBetterBasket
        }

        return result
