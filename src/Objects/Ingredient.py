import DataSource.DataSource as DataSource

class Ingredient:
    def __init__(self, id: int=None, name: str=""):
        self.id = id
        self.name = name
    
    @staticmethod
    def CreateIngredient(name: str) -> bool:
        if (not name) or (name.strip() == ""):
            print("Ingredient name cannot be empty")
            return False
        
        new_ingredient = Ingredient(name=name.strip())

        return DataSource.DataSource.AddIngredient(new_ingredient)
