import DataSource.LoadData as LoadData
from Recipe.Recipe import Recipe
from Ingredient.Ingredient import Ingredient

class DataSource:
    # ============= Recipes =============
    recipes = []
    @staticmethod
    def GetRecipes() -> list[Recipe]:
        if not DataSource.recipes:
            DataSource.recipes = LoadData.LoadRecipes()

        return DataSource.recipes
    
    @staticmethod
    def GetRecipeByID(id: int) -> Recipe | None:
        print(f"GetRecipeByID {id}")
        for recipe in DataSource.GetRecipes():
            if recipe.id == id:
                return recipe
        return None

    # ============= Ingredients =============
    ingredients = []
    @staticmethod
    def GetIngredients() -> list[Ingredient]:
        if not DataSource.ingredients:
            DataSource.ingredients = LoadData.LoadIngredients()

        return DataSource.ingredients
    
    @staticmethod
    def GetIngredientByID(id: int) -> Ingredient | None:
        print(f"GetIngredientByID {id}")
        for ingredient in DataSource.GetIngredients():
            if ingredient.id == id:
                return ingredient
        return None
