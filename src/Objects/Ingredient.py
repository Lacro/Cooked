import DataSource.DataSource as DataSource

class Ingredient:
    def __init__(self, id: int=None, name: str=""):
        self.id = id
        self.name = name

    def Validate(self):
        if not self.name: raise ValueError("Ingredient name cannot be empty")
        
        self.name=self.name.strip()
        
        if not self.name: raise ValueError("Ingredient name cannot be only whitespaces")
