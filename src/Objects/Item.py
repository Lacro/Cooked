import Objects.Units as Units
import Objects.Ingredient as Ingredient
import DataSource.DataSource as DataSource

class Item:
    def __init__(self, ingredient_id:int, quantity: int, unit: str):
        self.ingredient_id:int = ingredient_id
        self.quantity:int = quantity
        self.unit:str = unit
    
    def GetIngredient(self) -> Ingredient.Ingredient | None:
        return DataSource.DataSource.GetIngredientByID(self.ingredient_id)
    
    def GetIngredientName(self) -> str:
        ingredient = self.GetIngredient()

        return ingredient.name if ingredient else "Unknown Ingredient"
    
    def Validate(self):
        if self.unit == None: self.unit = ""
        self.unit=self.unit.strip()

        if not self.ingredient_id: raise ValueError("Ingredient ID is required")
        if self.quantity <= 0: raise ValueError("Quantity can't be less or equal to 0")
