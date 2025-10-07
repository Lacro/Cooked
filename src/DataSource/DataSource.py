from Recipe.Recipe import Recipe
import DataSource.LoadData as LoadData

class DataSource:
    recipes = []

    @staticmethod
    def GetRecipes() -> list[Recipe]:
        if not DataSource.recipes:
            DataSource.recipes = LoadData.LoadRecipes()
            
        return DataSource.recipes
    
    @staticmethod
    def GetRecipeByID(id: int) -> Recipe | None:
        for recipe in DataSource.recipes:
            if recipe.id == id:
                return recipe
        return None
