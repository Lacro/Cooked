import DataSource.DataSource as DataSource

class Ingredient:
    def __init__(self, id: int=None, name: str=""):
        self.id = id
        self.name = name
    
    @staticmethod
    def CreateIngredient(name: str):
        if not name:
            raise ValueError("Ingredient name cannot be None or empty")
        
        name=name.strip()

        if not name:
            raise ValueError("Ingredient name cannot be only whitespace")
        
        DataSource.DataSource.AddIngredient(Ingredient(name=name))

