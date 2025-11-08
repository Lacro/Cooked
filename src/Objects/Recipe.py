import Objects.Ingredient as Ingredient

class Recipe:
    def __init__(self, id: int, name: str, items:list[int]=[]):
        self.id:int = id
        self.name:str = name
        self.items:Ingredient = items
