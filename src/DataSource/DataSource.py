from __future__ import annotations

import DataSource.LoadData as LoadData
import Recipe.Recipe as Recipe
import Ingredient.Ingredient as Ingredient

class DataSource:
    # ============= Recipes =============
    recipes = []
    @staticmethod
    def GetRecipes() -> list[Recipe.Recipe]:
        if not DataSource.recipes:
            DataSource.recipes = LoadData.LoadRecipes()

        return DataSource.recipes
    
    @staticmethod
    def GetRecipeByID(id: int) -> Recipe.Recipe | None:
        print(f"GetRecipeByID {id}")
        for recipe in DataSource.GetRecipes():
            if recipe.id == id:
                return recipe
        return None

    # ============= Ingredients =============
    ingredients = []
    @staticmethod
    def GetIngredients() -> list[Ingredient.Ingredient]:
        if not DataSource.ingredients:
            DataSource.ingredients = LoadData.LoadIngredients()

        return DataSource.ingredients
    
    @staticmethod
    def GetIngredientByID(id: int) -> Ingredient.Ingredient | None:
        print(f"GetIngredientByID {id}")
        for ingredient in DataSource.GetIngredients():
            if ingredient.id == id:
                return ingredient
        return None
    
    @staticmethod
    def AddIngredient(ingredient: Ingredient):
        if ingredient not in DataSource.ingredients:
            DataSource.ingredients.append(ingredient)
