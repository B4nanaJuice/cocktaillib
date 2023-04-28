class Ingredient:
    def __init__(self, name: str, quantity: float):
        self.name = name
        self.quantity = quantity
        
    def toJSON(self):
        resp = {
            "name": self.name,
            "quantity": self.quantity
        }
        
        return resp