from __future__ import annotations

import DataSource.SupaBase as SupaBase
import Objects.Item as Item
import Objects.Recipe as Recipe
import Objects.Ingredient as Ingredient

class DataSource:
    @staticmethod
    async def Initialize(callback):
        def wrapped_callback():
            # Clear cached data
            DataSource.shoppingList = []
            # Call the user-defined callback
            callback()
        
        await SupaBase.Initialize(wrapped_callback)

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
            DataSource.ingredients = SupaBase.LoadIngredientsOrdered()
        
        # todo: optimisation
        if selection: return [ing for ing in DataSource.ingredients if ing.id in selection]
        else        : return DataSource.ingredients
    
    
    @staticmethod
    def GetIngredientsNotInShoppingList() -> list[Ingredient.Ingredient]:
        shopping_ingredient_ids = [item.ingredient_id for item in DataSource.GetShoppingList()]

        ret = [
            ingredient for ingredient in DataSource.GetIngredients()
            if ingredient.id not in shopping_ingredient_ids
        ]
        
        return ret
    
    @staticmethod
    def GetIngredientByID(id: int) -> Ingredient.Ingredient | None:
        for ingredient in DataSource.GetIngredients():
            if ingredient.id == id:
                return ingredient
        return None
    
    @staticmethod
    def AddIngredient(ingredient: Ingredient):
        DataSource.ingredients = [] # force reload on next access, todo: optimisation
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
            DataSource.shoppingList.sort(key=lambda x: x.GetIngredientName().lower())
        
        return DataSource.shoppingList

    @staticmethod
    def AddItemToShoppingList(item: Item.Item):
        DataSource.shoppingList = [] # force reload on next access, todo: optimisation
        SupaBase.AddItemToShoppingList(item)
    
    @staticmethod
    def RemoveItemFromShoppingList(ingredient_id: int):
        DataSource.shoppingList = [] # force reload on next access, todo: optimisation
        SupaBase.RemoveItemFromShoppingList(ingredient_id)
    
    @staticmethod
    def UpdateItemInShoppingList(item: Item.Item):
        DataSource.shoppingList = [] # force reload on next access, todo: optimisation
        SupaBase.UpdateItemInShoppingList(item)
    # ========================= Shopping =========================
    # ============================================================
