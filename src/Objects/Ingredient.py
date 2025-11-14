
class Ingredient:
    def __init__(self, id: int=None, name: str="", default_quantity: int=1, default_unit=""):
        self.id = id
        self.name = name
        self.default_quantity = default_quantity
        self.default_unit = default_unit

    def Validate(self):
        if self.name == None: self.name = ""
        self.name=self.name.strip()
        
        if self.default_unit == None: self.default_unit = ""
        self.default_unit=self.default_unit.strip()
        
        if not self.name: raise ValueError("Ingredient name cannot be only whitespaces")
        if self.default_quantity <= 0: raise ValueError("Default quantity can't be less or equal to 0")

