class Cocktail:
    def __init__(self, name: str, ingredients: list, drinkType: str, instructions: str = ""):
        self.name = name
        self.ingredients = ingredients
        self.drinkType = drinkType
        self.instructions = instructions
        
    def toJSON(self):
        resp = {
            "name": self.name,
            "ingredients": [],
            "drinkType": self.drinkType
            }
        
        for ing in self.ingredients:
            resp["ingredients"].append(ing.toJSON())
        
        if (self.instructions != ""):
            resp["instructions"] = self.instructions
            
        return resp
        