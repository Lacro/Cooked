import Objects.Units as Units
import Objects.Ingredient as Ingredient
import DataSource.DataSource as DataSource

class Item:
    def __init__(self, IngredientID:int, quantity: int, unit: str):
        self.ingredientID:int = IngredientID
        self.quantity:int = quantity
        self.unit:str = unit
    
    def GetIngredient(self) -> Ingredient.Ingredient | None:
        return DataSource.DataSource.GetIngredientByID(self.ingredientID)
    
    def GetIngredientName(self) -> str:
        ingredient = self.GetIngredient()

        return ingredient.name if ingredient else "Unknown Ingredient"
