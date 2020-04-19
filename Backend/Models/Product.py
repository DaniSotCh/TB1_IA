class Product:
    def __init__(self, name, price, weight, calories, fat, carbs, protein):
        super().__init__()
        #Products information
        #Calories	Fat (g)	Carbs (g)	Protein (g)
        self.name = name
        self.price = price
        self.weight = weight
        self.calories = calories
        self.fat = fat
        self.carbs = carbs
        self.protein = protein
    