from __future__ import annotations

import DataSource.SupaBase as SupaBase
import Objects.Item as Item
import Objects.Recipe as Recipe
import Objects.Ingredient as Ingredient

class DataSource:
    # ============================================================
    # ========================= Recipes ==========================
    recipes = []
    @staticmethod
    def GetRecipes() -> list[Recipe.Recipe]:
        if not DataSource.recipes:
            DataSource.recipes = SupaBase.LoadRecipes()

        return DataSource.recipes
    
    @staticmethod
    def GetRecipeByID(id: int) -> Recipe.Recipe | None:
        print(f"GetRecipeByID {id}")
        for recipe in DataSource.GetRecipes():
            if recipe.id == id:
                return recipe
        return None
    # ========================= Recipes ==========================
    # ============================================================


    # ============================================================
    # ======================== Ingredient ========================
    ingredients = []
    @staticmethod
    def GetIngredients(selection:list[int] = []) -> list[Ingredient.Ingredient]:
        if not DataSource.ingredients:
            DataSource.ingredients = SupaBase.LoadIngredients()
        
        # todo: optimisation
        if selection: return [ing for ing in DataSource.ingredients if ing.id in selection]
        else        : return DataSource.ingredients
    
    @staticmethod
    def GetIngredientByID(id: int) -> Ingredient.Ingredient | None:
        print(f"GetIngredientByID {id}")
        for ingredient in DataSource.GetIngredients():
            if ingredient.id == id:
                return ingredient
        return None
    
    @staticmethod
    def AddIngredient(ingredient: Ingredient):
        SupaBase.AddIngredient(ingredient)
    
    @staticmethod
    def GetNewIngredientId() -> int:
        # Generate a new ID (simple increment based on existing IDs)
        # todo : data persistence and more robust ID generation
        existing_ids = [ing.id for ing in DataSource.GetIngredients()]
        return max(existing_ids) + 1 if existing_ids else 1
    # ======================== Ingredient ========================
    # ============================================================


    # ============================================================
    # ========================= Shopping =========================
    shoppingList = []
    @staticmethod
    def GetShoppingList() -> list[Item.Item]:
        if not DataSource.shoppingList:
            DataSource.shoppingList = SupaBase.LoadShoppingList()
        
        return DataSource.shoppingList

    @staticmethod
    def AddItemToShoppingList(item: Item.Item):
        SupaBase.AddItemToShoppingList(item)
    
    @staticmethod
    def RemoveItemFromShoppingList(item_id: int):
        SupaBase.RemoveItemFromShoppingList(item_id)
    # ========================= Shopping =========================
    # ============================================================
